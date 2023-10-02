# ES6 Promises

### Install NodeJS 12.11.x
```
curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```
```
$ nodejs -v
v12.11.1
$ npm -v
6.11.3
```

### Install Jest, Babel, and ESLint
in your project directory:
```
Install Jest using: `npm install --save-dev jest`
Install Babel using: `npm install --save-dev babel-jest @babel/core @babel/preset-env @babel/cli`
Install ESLint using: `npm install --save-dev eslint`
```
and…
Don’t forget to run `$ npm install` when you have the package.json

### Response Data Format
uploadPhoto returns a response with the format
```
{
  status: 200,
  body: 'photo-profile-1',
}
```
createUser returns a response with the format
```
{
  firstName: 'Guillaume',
  lastName: 'Salva',
}
```



install semistandard:
```
npm install -g semistandard
```
run:
```
semistandard *.js --global
```
fix:
```
semistandard --fix *.js --global
```