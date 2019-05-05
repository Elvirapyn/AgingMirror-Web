
function Upload() {
     
 }

 Upload.prototype.listenUploadFiledEvent = function () {
   var  uploadBtn = $('#thumbnail-btn');
   uploadBtn.change(function () {
     var file = uploadBtn[0].files[0];
     var formData = new FormData();
     formData.append('img',file)
     xfzajax.post({
         'url':'',
         'data':formData,
         'processData':false,
         'contentType':false,
         'success':function (result) {
             console.log('ok')
          if(result['code']===200){
           console.log(result['data']);
          }
         }
     });
   });
 };

 Upload.prototype.run = function(){
    var self = this;
    self.listenUploadFiledEvent();
 };

 $(function () {
    var img = new Upload();
    img.run();
 });