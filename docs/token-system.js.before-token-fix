(function () {
  "use strict";

  const TOKEN_KEY = "formready_tokens";
  const HISTORY_KEY = "formready_token_history";

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
    "split-pdf": 25
  };

  const WITHDRAWALS = [
    { amount: 200, tokens: 20000 },
    { amount: 500, tokens: 50000 },
    { amount: 1000, tokens: 100000 },
    { amount: 5000, tokens: 500000 }
  ];

  function getTokens() {
    return Number(localStorage.getItem(TOKEN_KEY) || 0);
  }

  function saveTokens(value) {
    localStorage.setItem(TOKEN_KEY, String(value));
    updateWallet();
  }

  function addTokens(toolName) {
    const reward = REWARDS[toolName];
    if (!reward) return;

    const todayKey = "formready_reward_" + toolName + "_" +
      new Date().toISOString().slice(0, 10);

    if (localStorage.getItem(todayKey)) return;

    const newBalance = getTokens() + reward;
    saveTokens(newBalance);

    const history = JSON.parse(
      localStorage.getItem(HISTORY_KEY) || "[]"
    );

    history.unshift({
      type: "earn",
      tool: toolName,
      tokens: reward,
      date: new Date().toLocaleString()
    });

    localStorage.setItem(
      HISTORY_KEY,
      JSON.stringify(history.slice(0, 100))
    );

    localStorage.setItem(todayKey, "1");

    showToast("+" + reward + " 🪙 Tokens earned!");
  }

  function updateWallet() {
    document.querySelectorAll("[data-token-balance]").forEach(el => {
      el.textContent = getTokens().toLocaleString() + " 🪙";
    });
  }

  function showToast(message) {
    let toast = document.getElementById("token-toast");

    if (!toast) {
      toast = document.createElement("div");
      toast.id = "token-toast";
      toast.style.cssText =
        "position:fixed;bottom:20px;left:50%;transform:translateX(-50%);" +
        "background:#111;color:#fff;padding:12px 18px;border-radius:12px;" +
        "z-index:99999;font-weight:600;box-shadow:0 5px 20px #0004;";
      document.body.appendChild(toast);
    }

    toast.textContent = message;
    toast.style.display = "block";

    clearTimeout(window.__tokenToastTimer);

    window.__tokenToastTimer = setTimeout(() => {
      toast.style.display = "none";
    }, 2500);
  }

  window.FormReadyTokens = {
    getTokens,
    addTokens,
    updateWallet,
    rewards: REWARDS,
    withdrawals: WITHDRAWALS
  };

  document.addEventListener("DOMContentLoaded", updateWallet);
})();
