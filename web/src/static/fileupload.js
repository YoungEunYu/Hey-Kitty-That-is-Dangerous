function uploadFiles() {
    const fileInput = document.getElementById("fileInput");
    const files = fileInput.files;

    if (files.length === 0) {
        alert("이미지 파일을 선택하세요.");
        return;
    }

    const formData = new FormData();
    for (let i = 0; i < files.length; i++) {
        formData.append("photo", files[i]);
    }
    // Fetch API를 사용하여 파일들을 서버로 전송
    fetch("/fileupload", {
        method: "POST",
        body: formData
    })
    .then(response => response.text())
    .then(message => {
        const statusDiv = document.getElementById("status");
        statusDiv.innerText = message;
    })
    .catch(error => {
        console.error("파일 업로드 중 오류 발생:", error);
    });
}

//파일 삭제
function deleteFile(filename) {
    // Fetch API를 사용하여 파일 삭제 요청 보내기
    fetch('/delete', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `filename=${filename}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert(data.message);
            // 파일 삭제 후 페이지 새로고침 (선택사항)
            location.reload();
        } else if (data.error) {
            alert(`Error: ${data.error}`);
        }
    })
    .catch(error => {
        console.error('파일 삭제 중 오류 발생:', error);
    });
}

// 파일 선택과 업로드를 같이 처리하는 코드 추가
const fileInput = document.getElementById("fileInput");
fileInput.addEventListener("change", uploadFiles);

// 파일 삭제 버튼과 연결
const fileInputLabel = document.getElementById("fileInputLabel");
fileInputLabel.addEventListener("click", function() {
    fileInput.click();
});


// 파일 삭제 기능을 위해 추가한 코드
const fileList = document.getElementById("fileList");
fileList.addEventListener("click", function(event) {
    const target = event.target;
    if (target.tagName === "BUTTON") {
        const filename = target.getAttribute("data-filename");
        deleteFile(filename);
    }
});