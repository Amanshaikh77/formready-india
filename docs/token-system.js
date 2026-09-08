(function () {
  "use strict";

  const USER_KEY = "formready_user_key";

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

  let userKey =
    localStorage.getItem(USER_KEY) || "";

  async function api(path, options = {}) {

    options.headers = {
      ...(options.headers || {})
    };

    if (userKey) {
      options.headers["X-User-Key"] = userKey;
    }

    const response =
      await fetch("/api/token" + path, options);

    const data =
      await response.json();

    if (data.userKey) {
      userKey = data.userKey;

      localStorage.setItem(
        USER_KEY,
        userKey
      );
    }

    return data;
  }

  async function getTokens() {
    try {
      const data = await api("/balance");

      if (data.success) {
        return Number(data.tokens || 0);
      }
    } catch (error) {
      console.error("Token balance error:", error);
    }

    return 0;
  }

  async function updateWallet() {

    const tokens = await getTokens();

    document
      .querySelectorAll("[data-token-balance]")
      .forEach(el => {
        el.textContent =
          tokens.toLocaleString("en-IN") + " 🪙";
      });

    const balanceElement =
      document.getElementById("balance");

    if (balanceElement) {
      balanceElement.textContent =
        tokens.toLocaleString("en-IN");
    }

    return tokens;
  }

  async function addTokens(toolName) {

    const reward = REWARDS[toolName];

    if (!reward) {
      console.warn(
        "Unknown reward tool:",
        toolName
      );
      return false;
    }

    try {

      const data = await api("/earn", {
        method: "POST",

        headers: {
          "Content-Type": "application/json"
        },

        body: JSON.stringify({
          amount: reward,
          tool: toolName
        })
      });

      if (data.success) {

        showToast(
          "+" +
          data.earned +
          " 🪙 Tokens earned!"
        );

        await updateWallet();

        return true;
      }

      if (
        data.error ===
        "Reward already claimed today"
      ) {
        return false;
      }

      console.warn(
        "Token reward failed:",
        data.error
      );

      return false;

    } catch (error) {

      console.error(
        "Token earn error:",
        error
      );

      return false;
    }
  }

  function getReward(toolName) {
    return REWARDS[toolName] || 0;
  }

  function showToast(message) {

    let toast =
      document.getElementById("token-toast");

    if (!toast) {

      toast =
        document.createElement("div");

      toast.id = "token-toast";

      toast.style.cssText =
        "position:fixed;" +
        "bottom:20px;" +
        "left:50%;" +
        "transform:translateX(-50%);" +
        "background:#111;" +
        "color:#fff;" +
        "padding:12px 18px;" +
        "border-radius:12px;" +
        "z-index:99999;" +
        "font-weight:700;" +
        "box-shadow:0 5px 20px #0004;";

      document.body.appendChild(toast);
    }

    toast.textContent = message;
    toast.style.display = "block";

    clearTimeout(window.__tokenToastTimer);

    window.__tokenToastTimer =
      setTimeout(() => {
        toast.style.display = "none";
      }, 2500);
  }

  window.FormReadyTokens = {
    getTokens,
    addTokens,
    updateWallet,
    getReward,
    rewards: REWARDS
  };

  document.addEventListener(
    "DOMContentLoaded",
    updateWallet
  );

})();
