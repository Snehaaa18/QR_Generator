
document.getElementById("form").addEventListener("submit", function(event){
        event.preventDefault();
        var formData = new FormData(this);
        $.ajax({
            type: 'POST',
            url: 'main.py/ generate-qr',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                var img = document.getElementById('image-qr');
                var imageUrl = URL.createObjectURL(response);
                img.src = imageUrl;
                img.style.display = 'block';
            }
        });
    });
