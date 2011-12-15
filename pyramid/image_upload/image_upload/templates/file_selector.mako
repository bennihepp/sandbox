<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>jQuery File Upload Example</title>
</head>
<body>
<form id="fileupload" name="form">
	<input id="file" type="file" name="files" multiple />
</form>
<a href="#" id="upload">Upload</a>
<script src="../javascript/jquery.js"></script>
<script src="../javascript/jquery-ui.js"></script>
<script src="../javascript/jquery.iframe-transport.js"></script>
<script src="../javascript/jquery.fileupload.js"></script>
<script>
$(function () {
	var fileList = [];
    $('#fileupload').fileupload({
        dataType: 'json',
        url: 'upload',
        singleFileUploads: false,
        done: function (e, data) {
            $.each(data.result, function (index, file) {
                $('<p/>').text(file.name).appendTo(document.body);
            });
        }
    });
    $('#fileupload').fileupload({
    add: function (e, data) {
        //data.submit().error(function (jqXHR, textStatus, errorThrown) {
		//	alert("error: " + textStatus);
		//	alert(errorThrown);
		//});
		$.each(data.files, function (index, file) {
        	fileList.push(file);
    	});
    }
    });

    $('#upload').click(function () {
		$.each(fileList, function (index, file) {
	    	$('#fileupload').fileupload('send', {files: [file]})
	    	.error(function (jqXHR, textStatus, errorThrown) {
				alert("error: " + errorThrown);
			});
	    });
	});
});
</script>
</body> 
</html>

