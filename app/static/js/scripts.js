$(document).ready(function() {
  // Show modal in case of errors
  if (
    $("#user_name").hasClass("is-invalid") ||
    $("#user_phone").hasClass("is-invalid")
  ) {
    $("#exampleModal").modal("show");
  }
});
