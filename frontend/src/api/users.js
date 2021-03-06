import Axios from 'axios';
import Cookies from 'js-cookie';

const getUserProfile = async cmp => {
  const response = await Axios.get('/auth/users/me/', {
    headers: {
      Authorization: `JWT ${Cookies.get('jwtAccess')}`
    }
  });
  cmp.successProfileData(response);
  return response;
};

export { getUserProfile };
