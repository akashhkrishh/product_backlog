const STORAGE_KEY = 'appData';

export const localStorageService = {
  _getAppData() {
    const data = localStorage.getItem(STORAGE_KEY);
    return data ? JSON.parse(data) : { users: [], user: null };
  },

  _setAppData(data) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
  },

  saveUser(user) {
    const data = this._getAppData();

    if (data.users.find(u => u.email === user.email)) {
      alert("User with this email already exists.");
      return
    }

    data.users.push(user);
    data.user = user;
    this._setAppData(data);
  },


loginUser(id, password) {
  const data = this._getAppData();
  const existingUser = data.users.find(u => u.id == id && u.password === password);

  if (!existingUser) {
    alert("Invalid ID or password.");
    return null;
  }

  data.user = existingUser;
  this._setAppData(data);
  return existingUser;
},


  getCurrentUser() {
    return this._getAppData().user;
  },

 
  getAllUsers() {
    return this._getAppData().users;
  },

  logout() {
    const data = this._getAppData();
    data.user = null;
    this._setAppData(data);
  },

  clearAll() {
    localStorage.removeItem(STORAGE_KEY);
  }
};
