import { register } from '../services/AuthService.js'; 
import { attachFormHandler } from '../utilities/formHandler.js' 

export function initRegister() {
  attachFormHandler('#register-form', (data, form) => {
    register(data);
    form.reset();
  });
}
