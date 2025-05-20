import { login } from '../services/AuthService.js'; 
import { attachFormHandler } from '../utilities/formHandler.js' 

export function initLogin() {
  attachFormHandler('#login-form', (data, form) => {
    login(data);
    form.reset();
  });
}
