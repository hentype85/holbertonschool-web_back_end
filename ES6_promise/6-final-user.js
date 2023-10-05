import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default async function handleProfileSignup (firstName, lastName, fileName) {
  const res = [];

  try {
    const user = await signUpUser(firstName, lastName);
    const photo = await uploadPhoto(fileName);

    res.push({ status: 'fulfilled', value: user });
  } catch (err) {
    res.push({ status: 'rejected', value: err });
  }

  return res;
}
