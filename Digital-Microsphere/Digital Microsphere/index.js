// "use strict";
import * as THREE from 'three';
import { OrbitControls } from 'https://unpkg.com/three@^0.138.2/examples/jsm/controls/OrbitControls.js'
import { MTLLoader } from 'https://unpkg.com/three@^0.138.2/examples/jsm/loaders/MTLLoader.js';
import { OBJLoader } from 'https://unpkg.com/three@^0.138.2/examples/jsm/loaders/OBJLoader.js';

const renderer = new THREE.WebGLRenderer({ canvas: document.querySelector("canvas") });


const camera = new THREE.PerspectiveCamera(45, 2, 1, 2000);
camera.position.z = 5;

const scene = new THREE.Scene();
const size = 10;
const divisions = 25;
const gridHelper = new THREE.GridHelper(size, divisions);
scene.add(gridHelper);
const axesHelper = new THREE.AxesHelper(5);
scene.add(axesHelper);

const ambientLight = new THREE.AmbientLight(0xcccccc, 1.5);
scene.add(ambientLight);

const pointLight = new THREE.PointLight(0xffffff, 5000);
camera.add(pointLight);
var texture_name = localStorage.getItem('FileName');

const onProgress = function(xhr) {

    if (xhr.lengthComputable) {

        const percentComplete = xhr.loaded / xhr.total * 100;
        console.log(Math.round(percentComplete, 2) + '% downloaded');

    }

};
new MTLLoader()
    .setPath('./obj/')
    .load('emb_py_2.mtl', function(materials) {

        materials.preload();

        new OBJLoader()
            .setMaterials(materials)
            .setPath('./obj/')
            .load('emb.obj', function(object) {

                // object.position.y = -95;
                scene.add(object);

            }, onProgress);

    });
var controls = new OrbitControls(camera, renderer.domElement);



function resizeCanvasToDisplaySize() {
    const canvas = renderer.domElement;
    const width = canvas.clientWidth;
    const height = canvas.clientHeight;
    if (canvas.width !== width || canvas.height !== height) {
        // you must pass false here or three.js sadly fights the browser
        renderer.setSize(width, height, false);
        camera.aspect = width / height;
        camera.updateProjectionMatrix();

        // set render target sizes here
    }
}

function animate(time) {


    renderer.render(scene, camera);
    resizeCanvasToDisplaySize();
    requestAnimationFrame(animate);
}

requestAnimationFrame(animate);

const fileName1 = document.getElementById('file1');
const fileName2 = document.getElementById('file2');
const submit = document.getElementById('sub');

submit.addEventListener('click', () => {
    window.location.reload();
});
const { spawn } = require('child_process');
const importButton = document.getElementById('import');
importButton.addEventListener('click', importData);

function importData() {
    let input = document.createElement('input');
    input.type = 'file';
    input.multiple = true;
    input.onchange = _ => {
        // you can use this method to get file and perform respective operations
        let files = Array.from(input.files);

        const file_path1 = files[0].path;
        const file_path2 = files[1].path;
        fileName1.value = file_path1;
        fileName2.value = file_path2;
        const fs = require('fs');
        const child = spawn('python', ['initial.py', file_path1, file_path2]);
        child.stdout.on('data', (data) => {
            console.log(`stdout: ${data}`);
        });
        child.stderr.on('error', (e) => {
            console.log(`stderr: ${e}`);
        });
        child.on('close', (code) => {
            console.log(`child process exited with code ${code}`);
        });
        child.on('exit', (code) => {
            console.log(`child process exited with code ${code}`);
        });
        child.on('message', (message) => {
            console.log(`child process exited with code ${message}`);
        });
        child.on('disconnect', (message) => {
            console.log(`child process exited with code ${message}`);
        });

        fs.readFile("./obj/emb_py_2.mtl", 'utf8', function(err, data) {
            let searchString = 'map_Kd';
            let re = new RegExp('^.*' + searchString + '.*$', 'gm');
            let formatted = data.replace(re, searchString + ' ' + "outline.jpg");

            fs.writeFile("./obj/emb_py_2.mtl", formatted, 'utf8', function(err) {
                if (err) return console.log(err);
            });
        });

    };



    input.click();

}