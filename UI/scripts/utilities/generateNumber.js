import { localStorageService } from "../services/StorageService.js";
export function generate7DigitId() {
  const existingUsers = localStorageService.getAllUsers();
  const existingIds = new Set(existingUsers.map(user => user.id));

  let newId;
  do {
    newId = Math.floor(1000000 + Math.random() * 9000000);
  } while (existingIds.has(newId));

  return newId;
}
