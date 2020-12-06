import Controller from '@ember/controller';
import { inject as service } from '@ember/service';

export default Controller.extend({
    session: service('session'),
    actions: {
        logout() {
            this.session.logout();
            this.transitionToRoute('users');
        }
    }
});
