const show_edit_form_btn = document.getElementById('show_edit_form_btn');
const edit_form_container = document.getElementById('edit_form_container');

//event listener for click on edit button to show edit form
show_edit_form_btn.addEventListener('click', function () {
  console.log('working')
  if (edit_form_container.style.display === 'none' || edit_form_container.style.display === '') {
    edit_form_container.style.display = 'block';
  } else {
    edit_form_container.style.display = 'none';
  }
});