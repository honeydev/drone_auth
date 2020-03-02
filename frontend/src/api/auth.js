import Axios from 'axios';
import { catchAxiosException } from '../helpers/commonHelpers';

const sendLoginForm = async (cmp, formData) => {
  try {
    const response = await Axios.post('/auth/jwt/create/', formData);
    cmp.successLoginForm(response);
  } catch (error) {
    catchAxiosException(error, () => cmp.errorLoginForm(error.response));
  }
};

const sendRegisterForm = async (cmp, formData) => {
  try {
    const response = await Axios.post('/auth/users/', formData);
    cmp.handleSuccessRegisterForm(response);
    return response;
  } catch (error) {
    catchAxiosException(error, () =>
      cmp.hadnleErrorRegisterForm(error.response)
    );
  }
};

export { sendLoginForm, sendRegisterForm };
