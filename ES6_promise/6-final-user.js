import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default function handleProfileSignup (firstName, lastName, fileName) {
  const userPromise = signUpUser(firstName, lastName);
  const photoPromise = uploadPhoto(fileName);

  return Promise.all([userPromise, photoPromise])
    .then((data) => {
      ((data) => ({
        status: 'OK',
        value: result
      }));
    })
    .catch((data) => {
      ((data) => ({
        status: 'rejected',
        value: err
      }));
    });
}
