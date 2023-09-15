export default class HolbertonCourse {
    constructor(name, length, students) {
        this._name = name;
        this._length = length;
        this._students = students;
    }

    // getters
    get name() {
        return this._name;
    }
    get length() {
        return this._length;
    }
    get students() {
        return this._students;
    }

    // setters
    set name(newName) {
        if (typeof newName === 'string') {
            this._name = newName;
        }
    }
    set length(newLength) {
        if (typeof newLength === 'number') {
            this._length = newLength;
        }
    }
    set students(newStudents) {
        if (Array.isArray(newStudents)) {
            this._students = newStudents;
        }
    }
}

