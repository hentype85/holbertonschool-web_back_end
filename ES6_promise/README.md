# ES6 Promises

## Install NVM (Node Version Manager)
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
```

* Close and reopen the terminal to apply configuration changes.
* This step is important for NVM to work properly.

### Install NodeJS 12.11.x
```
curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```
```
node -v
npm -v
```

### Install Jest, Babel, and ESLint
in your project directory:
```
Install Jest using: `npm install --save-dev jest`
Install Babel using: `npm install --save-dev babel-jest @babel/core @babel/preset-env @babel/cli`
Install ESLint using: `npm install --save-dev eslint`
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