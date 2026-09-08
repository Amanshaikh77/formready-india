(function () {
  "use strict";

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

  function getToolName() {
    const path = location.pathname.toLowerCase();

    const match =
      path.match(/\/tools\/([^\/.]+)(?:\.html)?\/?$/);

    return match ? match[1] : "";
  }

  function getReward() {
    return REWARDS[getToolName()] || 0;
  }

  function isActionButton(button) {
    if (!button) return false;

    const text =
      (button.textContent || "").trim().toLowerCase();

    const id =
      (button.id || "").toLowerCase();

    return (
      text.includes("download") ||
      text.includes("crop & download") ||
      text.includes("generate") ||
      text.includes("create") ||
      text.includes("convert") ||
      text.includes("compress") ||
      text.includes("resize") ||
      text.includes("merge") ||
      text.includes("split") ||
      text.includes("passport") ||
      text.includes("signature") ||
      text.includes("sheet") ||
      id.includes("download") ||
      id.includes("generate") ||
      id.includes("convert")
    );
  }

  function addRewardLabel(button) {
    if (!button) return;

    const reward = getReward();

    if (!reward) return;

    if (button.dataset.rewardLabel === "1") {
      return;
    }

    button.dataset.rewardLabel = "1";

    const text =
      button.textContent.trim();

    if (/earn|tokens|🪙/i.test(text)) {
      return;
    }

    button.innerHTML =
      text +
      '<span class="fr-reward-text">' +
      '<br>🎁 Earn +' +
      reward +
      ' 🪙 Tokens' +
      '</span>';
  }

  function setupButton(button) {
    if (!isActionButton(button)) {
      return;
    }

    addRewardLabel(button);

    if (button.dataset.rewardClick === "1") {
      return;
    }

    button.dataset.rewardClick = "1";

    button.addEventListener("click", function () {

      const tool = getToolName();

      if (!tool || !REWARDS[tool]) {
        return;
      }

      setTimeout(function () {

        if (
          window.FormReadyTokens &&
          typeof window.FormReadyTokens.addTokens === "function"
        ) {
          window.FormReadyTokens.addTokens(tool);
        }

      }, 1200);
    });
  }

  function scanButtons() {
    document
      .querySelectorAll("button, a")
      .forEach(setupButton);
  }

  function addStyles() {

    if (
      document.getElementById(
        "fr-reward-button-style"
      )
    ) {
      return;
    }

    const style =
      document.createElement("style");

    style.id =
      "fr-reward-button-style";

    style.textContent = `
      .fr-reward-text {
        display: block;
        margin-top: 6px;
        font-size: 15px;
        font-weight: 800;
        line-height: 1.25;
      }
    `;

    document.head.appendChild(style);
  }

  function init() {
    addStyles();
    scanButtons();

    setTimeout(scanButtons, 500);
    setTimeout(scanButtons, 1500);
    setTimeout(scanButtons, 3000);

    const observer =
      new MutationObserver(function () {
        scanButtons();
      });

    observer.observe(document.body, {
      childList: true,
      subtree: true
    });
  }

  if (
    document.readyState === "loading"
  ) {
    document.addEventListener(
      "DOMContentLoaded",
      init
    );
  } else {
    init();
  }

  window.FormReadyRewardButtons = {
    getReward,
    refresh: scanButtons
  };

})();
