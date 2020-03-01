import _ from 'lodash';
import Cookies from 'js-cookie';

const isAuthTokenCookie = () => {
  return !_.isUndefined(Cookies.get('jwtAccess'));
};

export { isAuthTokenCookie };
