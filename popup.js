document.addEventListener('DOMContentLoaded', async () => {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    func: () => {
      return {
        html: document.documentElement.innerHTML,
        url: window.location.href
      };
    },
  }, async (results) => {
    const { html, url } = results[0].result;

    const response = await fetch("http://localhost:5000/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ html, url })
    });

    const data = await response.json();
    document.getElementById("results").innerText = JSON.stringify(data, null, 2);
  });
});
