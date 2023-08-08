const scrollArea = document.getElementById("scroll_area");
let warning_files = [];
function updateImages() {
    $.get('/get_images', function (data) {
        if (check_changed_file(warning_files, data)) {
            scrollArea.innerHTML = null;
            warning_files = manage_files(warning_files, data);
            warning_files.forEach((file) => {
                let divRecordContent = document.createElement('div');
                divRecordContent.classList.add("record_content_box");
                let divDetectTime = document.createElement('div');
                divDetectTime.classList.add("detectTime");
                divDetectTime.innerText = formatDate(file.slice(10, 24));

                let divAutoGroup = document.createElement('div');
                divAutoGroup.classList.add("auto-group-vzfb-Bdj");

                let divItemInm = document.createElement('div');
                divItemInm.classList.add("item--iNm");
                divItemInm.innerText = "인덕션에 접촉했어요!";
                divAutoGroup.appendChild(divItemInm);

                let imgElement = document.createElement('img');
                imgElement.classList.add('recent-images');
                imgElement.alt = "Most Recent Captured Image";
                imgElement.src = '/static/warnings/' + file;
                imgElement.style = "width:100%;";

                divRecordContent.appendChild(imgElement);
                divRecordContent.appendChild(divDetectTime);
                divRecordContent.appendChild(divAutoGroup);

                scrollArea.appendChild(divRecordContent);
            });
        }
    });
}

function formatDate(inputDate) {
    // Input date format: '20230804123807'
    // Convert the input date string to a JavaScript Date object
    const year = parseInt(inputDate.slice(0, 4));
    const month = parseInt(inputDate.slice(4, 6));
    const day = parseInt(inputDate.slice(6, 8));
    const hours = parseInt(inputDate.slice(8, 10));
    const minutes = parseInt(inputDate.slice(10, 12));
  
    const dateObject = new Date(year, month - 1, day, hours, minutes);
  
    // Format the date for desired output: '23.07.10 월 17:28시'
    const formattedDate = `${dateObject.getFullYear().toString().slice(2)}.${String(dateObject.getMonth() + 1).padStart(2, '0')}.${String(dateObject.getDate()).padStart(2, '0')} 월 ${String(dateObject.getHours()).padStart(2, '0')}:${String(dateObject.getMinutes()).padStart(2, '0')}시`;
  
    return formattedDate;
  }

function manage_files(files, value) {
    if (files.length >= 10) {
        files = files.slice(0, files.length - 1);
    }
    return [value, ...files];
}

function check_changed_file(files, value) {
    if (value === '') return false;
    return !files.includes(value);
}
// Update the images every 3 seconds (adjust the interval as needed)
setInterval(updateImages, 3000);