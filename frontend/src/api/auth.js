import Axios from 'axios';

const sendLoginForm = async (cmp, formData) => {
  try {
    const response = await Axios.post('/auth/jwt/create/', formData);
    cmp.successLoginForm(response);
  } catch (error) {
    cmp.errorLoginForm(error.response);
    console.log(error);
  }
};

const sendRegisterForm = async (cmp, formData) => {
  try {
    const response = await Axios.post('/auth/users/', formData);
    cmp.successRegisterForm(response);
  } catch (error) {
    console.log(error);
  }
};

export { sendLoginForm, sendRegisterForm };
