document.addEventListener("DOMContentLoaded", function () {
  const channelListElement = document.getElementById("channelList");
  const CHANNEL_ICON_PATH = "../static/img/icon_pows.svg";

  // チャンネルリストを取得して表示する関数
  function fetchChannels() {
    fetch("/channels") // Flaskのエンドポイントを適宜修正してください
      .then((response) => response.json())
      .then((data) => {
        channelListElement.innerHTML = "";
        data.forEach((channel) => {
          const channelItem = document.createElement("div");
          channelItem.classList.add("channel-item");

          // アイコンを表示するimg要素を作成
          const iconImg = document.createElement("img");
          iconImg.src = CHANNEL_ICON_PATH;
          iconImg.alt = "Channel Icon";
          iconImg.classList.add("channel-icon");

          // チャンネル名を表示するa要素を作成
          const channelLink = document.createElement("a");
          channelLink.href = `detail.html?channelId=${channel.id}`;
          channelLink.textContent = channel.name;
          channelLink.classList.add("channel-name");

          // 削除ボタンの作成
          const deleteButton = document.createElement("button");
          deleteButton.innerText = "削除";
          deleteButton.classList.add("delete-button");
          deleteButton.onclick = function () {
            if (confirm("このチャンネルを削除しますか？")) {
              fetch(`/delete/${channel.id}`, { method: "POST" }) // Flaskのエンドポイントを適宜修正してください
                .then(() => {
                  channelItem.remove();
                })
                .catch((error) => {
                  console.error("Error:", error);
                });
            }
          };
          // チャンネル項目にアイコン、リンク、削除ボタンを追加
          channelItem.appendChild(iconImg);
          channelItem.appendChild(channelLink);
          channelItem.appendChild(deleteButton);

          // 完成したチャンネル項目リストを追加
          channelListElement.appendChild(channelItem);
        });
      });
  }

  // チャンネルリストを取得
  fetchChannels();

  // チャンネル追加のフォーム送信イベントを処理
  document.getElementById("channel-form").onsubmit = function (event) {
    event.preventDefault();
    const formData = new FormData(this);
    fetch("/", { method: "POST", body: formData })
      .then((response) => {
        if (!response.ok) {
          throw new Error("サーバーエラーが発生しました");
        }
        fetchChannels(); // リストを再取得して表示を更新
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };
});
