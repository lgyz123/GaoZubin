---
title: "投稿"
menu:
  main:
    weight: 40
---

<form id="submit-form" method="POST" action="ACTION_URL" enctype="multipart/form-data">
  <p>
    这个页面只用来<strong>提交新画作信息</strong>。提交后不会自动公开，需要管理员整理后发布到画廊。
  </p>

  <label for="title">画作标题（必填）</label><br>
  <input id="title" type="text" name="title" required style="width:100%;padding:8px;margin:4px 0 12px;border:1px solid #ccc;border-radius:4px;box-sizing:border-box;">

  <label for="description">画作简介 / 说明（必填）</label><br>
  <textarea id="description" name="description" required
    style="width:100%;min-height:90px;padding:8px;margin:4px 0 12px;border:1px solid #ccc;border-radius:4px;box-sizing:border-box;"></textarea>

  <div style="font-size:0.9rem;color:#666;margin:-8px 0 12px;">
    例如：创作时间、尺幅、纸张 / 颜料、想表达的意境等等。
  </div>

  <!-- 拖拽上传区域 -->
  <label>画作图片（必填，支持多张）</label>
  <div id="dropzone" style="
      border:2px dashed #bbb;
      border-radius:8px;
      padding:24px 12px;
      text-align:center;
      margin:4px 0 8px;
      background:#fafafa;
      cursor:pointer;
      transition:background 0.2s,border-color 0.2s;
    ">
    将图片拖拽到这里，或点击选择文件<br>
    <span style="font-size:0.85rem;color:#777;">支持 JPG / PNG，最多若干张（具体上限看你表单服务限制）</span>
  </div>

  <!-- 真正的文件 input，隐藏掉，依然会随表单提交 -->
  <input id="file-input" type="file" name="images" accept="image/*" multiple style="display:none;">

  <ul id="file-list" style="font-size:0.85rem;color:#555;margin:4px 0 12px 18px;padding:0;list-style:disc;"></ul>

  <label for="contact">联系信息（选填）</label><br>
  <input id="contact" type="text" name="contact" placeholder="邮箱 / 微信 / 电话都可以"
    style="width:100%;padding:8px;margin:4px 0 12px;border:1px solid #ccc;border-radius:4px;box-sizing:border-box;">

  <label for="note">其他备注（选填）</label><br>
  <textarea id="note" name="note"
    style="width:100%;min-height:70px;padding:8px;margin:4px 0 16px;border:1px solid #ccc;border-radius:4px;box-sizing:border-box;"></textarea>

  <button type="submit" style="
      padding:8px 18px;
      border:none;
      border-radius:4px;
      background:#333;
      color:#fff;
      font-size:0.9rem;
      cursor:pointer;
    ">
    提交
  </button>

  <div id="success" style="
      display:none;
      margin-top:12px;
      padding:10px 12px;
      border-radius:4px;
      background:#e6ffed;
      border:1px solid #b7eb8f;
      color:#135200;
      font-size:0.85rem;
    ">
    已提交成功。管理员整理后，如适合，会发布到画廊页面。
  </div>
</form>

<script>
  const dropzone = document.getElementById('dropzone');
  const fileInput = document.getElementById('file-input');
  const fileList = document.getElementById('file-list');
  const form = document.getElementById('submit-form');
  const successBox = document.getElementById('success');

  function updateFileList() {
    fileList.innerHTML = '';
    const files = fileInput.files;
    if (!files || files.length === 0) {
      return;
    }
    for (let i = 0; i < files.length; i++) {
      const li = document.createElement('li');
      const sizeKB = Math.round(files[i].size / 1024);
      li.textContent = files[i].name + ' (' + sizeKB + ' KB)';
      fileList.appendChild(li);
    }
  }

  dropzone.addEventListener('click', function () {
    fileInput.click();
  });

  dropzone.addEventListener('dragover', function (e) {
    e.preventDefault();
    dropzone.style.background = '#f0f9ff';
    dropzone.style.borderColor = '#66a3ff';
  });

  dropzone.addEventListener('dragleave', function (e) {
    e.preventDefault();
    dropzone.style.background = '#fafafa';
    dropzone.style.borderColor = '#bbb';
  });

  dropzone.addEventListener('drop', function (e) {
    e.preventDefault();
    dropzone.style.background = '#fafafa';
    dropzone.style.borderColor = '#bbb';

    const dt = new DataTransfer();
    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      for (let i = 0; i < e.dataTransfer.files.length; i++) {
        dt.items.add(e.dataTransfer.files[i]);
      }
      fileInput.files = dt.files;
      updateFileList();
    }
  });

  fileInput.addEventListener('change', updateFileList);

  // 如果你用的是支持跨域的表单服务，可以用 fetch 拦截提交
  form.addEventListener('submit', function (e) {
    // 如果你想让表单正常跳转（比如表单服务自带成功页面），就把下面这块注释掉
    e.preventDefault();

    const formData = new FormData(form);

    fetch(form.action, {
      method: 'POST',
      body: formData
    }).then(function (res) {
      if (res.ok) {
        successBox.style.display = 'block';
        form.reset();
        fileList.innerHTML = '';
      } else {
        alert('提交失败，请稍后再试。');
      }
    }).catch(function () {
      alert('网络错误，提交未成功。');
    });
  });
</script>
