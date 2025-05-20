import { User } from "../entities/User.js";
import { generate7DigitId } from "../utilities/generateNumber.js";
import { localStorageService } from "./StorageService.js";
export function register(data) {
  const newUser = new User();
  newUser.id = generate7DigitId();
  newUser.name = data.name;
  newUser.email = data.email;
  newUser.address = data.address;
  newUser.password = data.password;
  localStorageService.saveUser(newUser);

}

export function login(data) {

  localStorageService.loginUser(data.id,data.password);
}
