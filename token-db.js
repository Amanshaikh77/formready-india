const fs = require("fs");
const path = require("path");
const crypto = require("crypto");

const DB_FILE = path.join(__dirname, "tokens.json");

function loadDB() {
    if (!fs.existsSync(DB_FILE)) {
        const initial = {
            users: {},
            history: []
        };
        fs.writeFileSync(DB_FILE, JSON.stringify(initial, null, 2));
        return initial;
    }

    try {
        return JSON.parse(fs.readFileSync(DB_FILE, "utf8"));
    } catch {
        return { users: {}, history: [] };
    }
}

function saveDB(db) {
    fs.writeFileSync(DB_FILE, JSON.stringify(db, null, 2));
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

function addTokens(userKey, amount, tool = "unknown") {
    const db = loadDB();
    const user = getUser(userKey);

    user.tokens += Number(amount);
    user.updatedAt = new Date().toISOString();

    db.history.push({
        userKey,
        tool,
        type: "earn",
        tokens: Number(amount),
        createdAt: new Date().toISOString()
    });

    saveDB(db);

    return user.tokens;
}

function spendTokens(userKey, amount, tool = "unknown") {
    const db = loadDB();
    const user = getUser(userKey);
    const cost = Number(amount);

    if (user.tokens < cost) {
        return {
            success: false,
            balance: user.tokens
        };
    }

    user.tokens -= cost;
    user.updatedAt = new Date().toISOString();

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

module.exports = {
    createUser,
    getUser,
    getTokens,
    addTokens,
    spendTokens
};
