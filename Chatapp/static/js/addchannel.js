function addChannel() {
    var channelList = document.getElementById('channelList');
    var channelNameInput = document.getElementById('channelName');
    var channelName = channelNameInput.value.trim();

    if (channelName) {
      // 新しいチャンネル項目を作成
        var newItem = document.createElement('div');
        newItem.className = 'channel-item';
        newItem.textContent = channelName;

        // 削除ボタンを作成
        var deleteBtn = document.createElement('button');
        deleteBtn.textContent = '削除';
        deleteBtn.className = 'delete-btn';
        deleteBtn.onclick = function() {
            channelList.removeChild(newItem);
        };

        // 項目に削除ボタンを追加
        newItem.appendChild(deleteBtn);

        // チャンネルリストに項目を追加
        channelList.appendChild(newItem);

        // 入力フィールドをクリア
        channelNameInput.value = '';
    } else {
        alert('チャンネル名を入力してください。');
    }
    }
