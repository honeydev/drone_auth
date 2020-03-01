import _ from 'lodash';
import Cookies from 'js-cookie';

const isAuthTokenCookie = () => {
  return !_.isUndefined(Cookies.get('jwtAccess'));
};

const setAuntState = (tokens, store) => {
  const expireDt = new Date(Date.now());
  expireDt.setHours(expireDt.getHours() + 2);
  Cookies.set('jwtAccess', tokens.access, { expires: expireDt });
  Cookies.set('jwtRefresh', tokens.refresh, { expires: expireDt });
  store.commit('switchAuth');
};

const removeAuthState = store => {
  Cookies.remove('jwtAccess');
  Cookies.remove('jwtRefresh');
  store.commit('switchAuth');
};

export { isAuthTokenCookie, setAuntState, removeAuthState };
