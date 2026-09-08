const express = require("express");
const path = require("path");
const fs = require("fs");
const crypto = require("crypto");

const tokenDB = require("./token-db");

const app = express();
const PORT = 3000;

const PUBLIC = path.join(__dirname, "public");

app.use(express.json({ limit: "50mb" }));
app.use(express.urlencoded({ extended: true, limit: "50mb" }));

app.use(express.static(PUBLIC));

/* =========================
   USER ID / TOKEN SYSTEM
========================= */

function getUserKey(req, res) {
    let userKey = req.headers["x-user-key"];

    if (!userKey) {
        userKey = crypto.randomUUID();
    }

    res.setHeader("X-User-Key", userKey);

    tokenDB.getUser(userKey);

    return userKey;
}

/* Get balance */
app.get("/api/token/balance", (req, res) => {
    try {
        const userKey = getUserKey(req, res);

        res.json({
            success: true,
            userKey,
            tokens: tokenDB.getTokens(userKey)
        });
    } catch (error) {
        console.error(error);
        res.status(500).json({
            success: false,
            error: "Unable to get token balance"
        });
    }
});

/* Earn tokens */
app.post("/api/token/earn", (req, res) => {
    try {
        const userKey = getUserKey(req, res);

        const amount = Number(req.body.amount || 0);
        const tool = String(req.body.tool || "unknown-tool");

        if (!Number.isFinite(amount) || amount <= 0) {
            return res.status(400).json({
                success: false,
                error: "Invalid token amount"
            });
        }

        const balance = tokenDB.addTokens(userKey, amount, tool);

        res.json({
            success: true,
            earned: amount,
            balance
        });
    } catch (error) {
        console.error(error);
        res.status(500).json({
            success: false,
            error: "Unable to add tokens"
        });
    }
});

/* Spend tokens */
app.post("/api/token/spend", (req, res) => {
    try {
        const userKey = getUserKey(req, res);

        const amount = Number(req.body.amount || 0);
        const tool = String(req.body.tool || "unknown-tool");

        if (!Number.isFinite(amount) || amount <= 0) {
            return res.status(400).json({
                success: false,
                error: "Invalid token amount"
            });
        }

        const result = tokenDB.spendTokens(
            userKey,
            amount,
            tool
        );

        if (!result.success) {
            return res.status(402).json({
                success: false,
                error: "Not enough tokens",
                balance: result.balance
            });
        }

        res.json({
            success: true,
            spent: amount,
            balance: result.balance
        });
    } catch (error) {
        console.error(error);
        res.status(500).json({
            success: false,
            error: "Unable to spend tokens"
        });
    }
});

/* =========================
   HOME PAGE
========================= */

app.get("/", (req, res) => {
    res.sendFile(path.join(PUBLIC, "index.html"));
});

/* =========================
   FOLDER BASED TOOLS
========================= */

app.get("/tools/:tool/", (req, res, next) => {
    const tool = req.params.tool;

    if (!/^[a-zA-Z0-9_-]+$/.test(tool)) {
        return res.status(400).send("Invalid tool name");
    }

    const file = path.join(
        PUBLIC,
        "tools",
        tool,
        "index.html"
    );

    if (fs.existsSync(file)) {
        return res.sendFile(file);
    }

    next();
});

/* =========================
   DIRECT HTML TOOLS
========================= */

app.get("/tools/:tool.html", (req, res, next) => {
    const tool = req.params.tool;

    if (!/^[a-zA-Z0-9_-]+$/.test(tool)) {
        return res.status(400).send("Invalid tool name");
    }

    const file = path.join(
        PUBLIC,
        "tools",
        tool + ".html"
    );

    if (fs.existsSync(file)) {
        return res.sendFile(file);
    }

    next();
});

/* =========================
   404
========================= */

app.use((req, res) => {
    res.status(404).send(`
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>404 | FormReady India</title>
<style>
body{
    margin:0;
    min-height:100vh;
    display:flex;
    align-items:center;
    justify-content:center;
    font-family:Arial,sans-serif;
    background:#f4f7fb;
    color:#111827;
    text-align:center;
}
.box{
    background:white;
    padding:35px;
    border-radius:20px;
    box-shadow:0 10px 35px #0001;
}
h1{
    font-size:64px;
    margin:0;
}
p{
    color:#64748b;
}
a{
    display:inline-block;
    margin-top:15px;
    padding:12px 22px;
    border-radius:10px;
    background:#2563eb;
    color:white;
    text-decoration:none;
    font-weight:bold;
}
</style>
</head>
<body>
<div class="box">
<h1>404</h1>
<p>Page not found</p>
<a href="/">Go Home</a>
</div>
</body>
</html>
`);
});

/* =========================
   START SERVER
========================= */

app.listen(PORT, "0.0.0.0", () => {
    console.log("");
    console.log("================================");
    console.log("        FormReady India");
    console.log("        SERVER RUNNING");
    console.log("================================");
    console.log("");
    console.log("Local: http://127.0.0.1:" + PORT);
    console.log("");
});
