export class User {
  constructor(name, password, role = 'user',address,email) {
    this.name = name;
    this.address = address;
    this.password = password;
    this.email = email
    this.role = role;
  }
}
