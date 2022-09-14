const { app, BrowserWindow, Menu } = require('electron')
    // const { Path } = require('three')
const path = require('path')
const windows = new Set();
// const submit = document.getElementById('sub');
const createWindow = () => {
    const win = new BrowserWindow({
        show: false,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false
        }
    })
    win.maximize()
    win.show()
    win.loadFile(path.join(__dirname, 'index.html'))

    win.on('closed', function() {
            app.quit();
        })
        // const submit = document.getElementById('sub');
        // submit.addEventListener('click', () => {
        //     win.reload();
        // })
    windows.add(win)

}

app.whenReady().then(() => {
    createWindow()
    const mainMenu = Menu.buildFromTemplate(mainMenuTemplate);
    Menu.setApplicationMenu(mainMenu);


})

function load_window() {
    const win1 = new BrowserWindow({
        width: 400,
        height: 600,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false
        }
    })
    const mainMenu_load = Menu.buildFromTemplate(mainMenuTemplate1);
    // Menu.setApplicationMenu(mainMenu_load);
    win1.setMenu(mainMenu_load);
    win1.loadFile(path.join(__dirname, 'index.html'))

    // submit.addEventListener('click', () => {
    //     createWindow();
    // });
    windows.add(win1)
}

function cellView() {
    const win = new BrowserWindow({
        width: 1200,
        height: 600
    })

    win.loadFile(path.join(__dirname, 'index.html'))
}

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit()
})

const mainMenuTemplate = [{
        label: 'File',
        submenu: [{
            label: 'Quit',
            accelerator: process.platform == 'darwin' ? 'Command+Q' : 'Ctrl+Q',
            click() {
                app.quit();
            }
        }],

    },
    {
        label: 'Cell View',
        submenu: [{
            label: 'See Cell View',
            accelerator: process.platform == 'darwin' ? 'Command+W' : 'Ctrl+W',
            click() {
                cellView();
            }
        }]
    },
    {
        label: 'Load Model',
        submenu: [{
            label: 'See Cell View',
            accelerator: process.platform == 'darwin' ? 'Command+N' : 'Ctrl+N',
            click() {
                load_window();
            }
        }]
    }
];

if (process.env.NODE_ENV !== 'production') {
    mainMenuTemplate.push({
        label: 'Developer Tools',
        submenu: [{
                label: 'Toggle DevTools',
                accelerator: process.platform == 'darwin' ? 'Command+I' : 'Ctrl+I',
                click(item, focusedWindow) {
                    focusedWindow.toggleDevTools();
                }
            }, {
                role: 'reload'
            }

        ]
    });
}


const mainMenuTemplate1 = [{
    label: 'File',
    submenu: [{
        label: 'Quit',
        accelerator: process.platform == 'darwin' ? 'Command+Q' : 'Ctrl+Q',
        click() {
            app.quit();
        }
    }],

}];

if (process.env.NODE_ENV !== 'production') {
    mainMenuTemplate1.push({
        label: 'Developer Tools',
        submenu: [{
                label: 'Toggle DevTools',
                accelerator: process.platform == 'darwin' ? 'Command+I' : 'Ctrl+I',
                click(item, focusedWindow) {
                    focusedWindow.toggleDevTools();
                }
            }, {
                role: 'reload'
            }

        ]
    });
}
console.log(windows);