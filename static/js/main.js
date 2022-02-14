alert("developing 2022/02/14");
$("#btn1").on("click", function()  {
  let date = new Date();
  let year = date.getFullYear();
  let month = date.getMonth() + 1;
  let day = date.getDate();
  let message = `${year}${month}${day}`
  $("#tBox").val(message);
});

$(".menu").on('click', function() {
     this.classList.toggle('toggle');
});