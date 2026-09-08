const fs = require("fs");
const path = require("path");
const crypto = require("crypto");

const DB_FILE = path.join(__dirname, "tokens.json");

const REWARDS = {
    "jpg-to-pdf": 20,
    "merge-pdf": 25,
    "passport-photo": 25,
    "pdf-compressor": 25,
    "pdf-to-jpg": 20,
    "photo-compressor": 20,
    "photo-resizer": 20,
    "photo-sheet": 25,
    "signature-maker": 20,
    "split-pdf": 25,
    "crop": 40
};

function loadDB() {
    if (!fs.existsSync(DB_FILE)) {
        const initial = {
            users: {},
            history: [],
            withdrawals: []
        };

        fs.writeFileSync(
            DB_FILE,
            JSON.stringify(initial, null, 2)
        );

        return initial;
    }

    try {
        const db = JSON.parse(
            fs.readFileSync(DB_FILE, "utf8")
        );

        db.users = db.users || {};
        db.history = db.history || [];
        db.withdrawals = db.withdrawals || [];

        return db;

    } catch {
        return {
            users: {},
            history: [],
            withdrawals: []
        };
    }
}

function saveDB(db) {
    fs.writeFileSync(
        DB_FILE,
        JSON.stringify(db, null, 2)
    );
}

function createUser() {
    const db = loadDB();

    const userKey = crypto.randomUUID();

    db.users[userKey] = {
        tokens: 0,
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString()
    };

    saveDB(db);

    return userKey;
}

function getUser(userKey) {
    const db = loadDB();

    if (!db.users[userKey]) {
        db.users[userKey] = {
            tokens: 0,
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
        };

        saveDB(db);
    }

    return db.users[userKey];
}

function getTokens(userKey) {
    return getUser(userKey).tokens;
}

/*
================================================
EARN TOKENS
================================================

No daily limit.

Every successful tool use can earn its reward.
The reward amount is controlled here on server side.
The client cannot choose 999 tokens.
*/

function addTokens(userKey, amount, tool = "unknown") {

    const db = loadDB();

    if (!db.users[userKey]) {
        db.users[userKey] = {
            tokens: 0,
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
        };
    }

    const user = db.users[userKey];

    const reward =
        REWARDS[tool];

    if (!reward) {
        return {
            success: false,
            error: "Invalid reward tool",
            earned: 0,
            balance: user.tokens
        };
    }

    user.tokens += reward;

    user.updatedAt =
        new Date().toISOString();

    db.history.push({
        userKey,
        tool,
        type: "earn",
        tokens: reward,
        createdAt: new Date().toISOString()
    });

    saveDB(db);

    return {
        success: true,
        earned: reward,
        balance: user.tokens
    };
}

/*
================================================
SPEND TOKENS
================================================
*/

function spendTokens(
    userKey,
    amount,
    tool = "unknown"
) {

    const db = loadDB();

    const user =
        db.users[userKey];

    if (!user) {
        return {
            success: false,
            error: "User not found",
            balance: 0
        };
    }

    const cost =
        Number(amount);

    if (
        !Number.isFinite(cost) ||
        cost <= 0
    ) {
        return {
            success: false,
            error: "Invalid token amount",
            balance: user.tokens
        };
    }

    if (user.tokens < cost) {
        return {
            success: false,
            error: "Not enough tokens",
            balance: user.tokens
        };
    }

    user.tokens -= cost;

    user.updatedAt =
        new Date().toISOString();

    db.history.push({
        userKey,
        tool,
        type: "spend",
        tokens: cost,
        createdAt: new Date().toISOString()
    });

    saveDB(db);

    return {
        success: true,
        balance: user.tokens
    };
}

function createWithdrawal(
    userKey,
    amount,
    upi
) {

    const db = loadDB();

    const user =
        db.users[userKey];

    if (!user) {
        return {
            success: false,
            error: "User not found"
        };
    }

    const tokensRequired =
        Number(amount) * 100;

    if (
        !Number.isFinite(tokensRequired) ||
        tokensRequired <= 0
    ) {
        return {
            success: false,
            error: "Invalid withdrawal amount"
        };
    }

    if (user.tokens < tokensRequired) {
        return {
            success: false,
            error: "Not enough tokens",
            balance: user.tokens
        };
    }

    user.tokens -= tokensRequired;

    user.updatedAt =
        new Date().toISOString();

    const withdrawal = {
        id: crypto.randomUUID(),
        userKey,
        amount: Number(amount),
        tokens: tokensRequired,
        upi: String(upi),
        status: "pending",
        createdAt: new Date().toISOString()
    };

    db.withdrawals.push(
        withdrawal
    );

    db.history.push({
        userKey,
        type: "withdrawal",
        tokens: tokensRequired,
        amount: Number(amount),
        createdAt: new Date().toISOString()
    });

    saveDB(db);

    return {
        success: true,
        withdrawal,
        balance: user.tokens
    };
}

function getWithdrawals() {
    return loadDB().withdrawals || [];
}

function updateWithdrawal(
    id,
    status
) {

    const db = loadDB();

    const withdrawal =
        db.withdrawals.find(
            w => w.id === id
        );

    if (!withdrawal) {
        return {
            success: false,
            error: "Withdrawal not found"
        };
    }

    withdrawal.status =
        status;

    withdrawal.updatedAt =
        new Date().toISOString();

    saveDB(db);

    return {
        success: true,
        withdrawal
    };
}

module.exports = {
    createUser,
    getUser,
    getTokens,
    addTokens,
    spendTokens,
    createWithdrawal,
    getWithdrawals,
    updateWithdrawal,
    REWARDS
};
