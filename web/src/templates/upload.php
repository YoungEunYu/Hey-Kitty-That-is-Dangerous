<?php
$targetDir = "uploads/";
$uploadOk = 1;

// 여러 개의 파일 처리
if(isset($_FILES["uploadFiles"])) {
    $files = $_FILES["uploadFiles"];
    $totalFiles = count($files["name"]);

    for ($i = 0; $i < $totalFiles; $i++) {
        $targetFile = $targetDir . basename($files["name"][$i]);
        $imageFileType = strtolower(pathinfo($targetFile, PATHINFO_EXTENSION));

        // 파일 유효성 검사
        $check = getimagesize($files["tmp_name"][$i]);
        if ($check !== false) {
            echo "파일은 이미지입니다. - " . $check["mime"] . ".";
            $uploadOk = 1;
        } else {
            echo "파일은 이미지가 아닙니다.";
            $uploadOk = 0;
        }

        // 파일 업로드
        if ($uploadOk == 0) {
            echo "파일 업로드 실패";
        } else {
            if (move_uploaded_file($files["tmp_name"][$i], $targetFile)) {
                echo "파일 " . basename($files["name"][$i]) . "이(가) 업로드되었습니다.";
            } else {
                echo "파일 업로드 실패";
            }
        }
    }
}
?>