var is_preview = false;
var image_file;

function preview(input) {
  image_file = $("input[type=file]").get(0).files[0];

  if (image_file) {
    $('#caution').hide();
    var reader = new FileReader();

    reader.onload = function(){
      $("#preview_img").attr("src", reader.result);
    }

    reader.readAsDataURL(image_file);
    is_preview = true;
  }
}

function upload() {
  if (image_file) {
    var fileType = image_file["type"];
    var validImageTypes = ["image/jpeg", "image/png"];
    if ($.inArray(fileType, validImageTypes) < 0) {
      Swal.fire('Only Accept Image');
      return;
    }

    var form_data = new FormData();
    form_data.append('file', $('#photo').prop('files')[0]);

    $.ajax({
        type: "POST",
        url: $HOST_API + '/upload/image',
        data: form_data,
        contentType: false,
        cache: false,
        processData: false,
        success: function(response) {
          console.log("SUcess");
        },
        error: function(err) {
            console.log(err);
        }
    });

  } else {
    Swal.fire('Please select an image');
    return;
  }
}

function clear_img() {
  document.getElementById('photo').value = "";
  $("#preview_img").attr("src", "#");
  $('#caution').show();
  image_file = null;
}
