import { Middleware } from '@nuxt/types';

const authenticated: Middleware = (context) => {
    if (context.store.state.auth_token == '') {
        return context.redirect('/');
    }
};

export default authenticated;