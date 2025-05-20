export function validateForm(form) {
  let isValid = true;
  return isValid;
}

export function getFormData(form) {
  const formData = new FormData(form);
  const data = {};
  for (const [key, value] of formData.entries()) {
    data[key] = value;
  }
  return data;
}

export function attachFormHandler(formSelector, callback) {
  const form = document.querySelector(formSelector);
  if (!form) {
    // console.warn(`Form with selector "${formSelector}" not found.`);
    return;
  }

  form.addEventListener('submit', event => {
    event.preventDefault();

    if (!validateForm(form)) {
      alert('Please fill all required fields correctly.');
      return;
    }

    const data = getFormData(form);
    callback(data, form);
  });
}