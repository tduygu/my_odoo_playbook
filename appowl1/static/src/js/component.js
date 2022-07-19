odoo.define('appowl1.component', function(require){
    "use strict";
    const { Component } = owl;
    const { xml } = owl.tags;

    class AppowlComponent extends Component {
        static template = xml`
        <div class="bg-info text-center p-2">
            <b> Welcome my friend </b>
            <i class="fa fa-close p-1 float-right" style="cursor: pointer;" t-on-click="onRemove"> </i>
        </div>`
        onRemove(ev) {
            this.destroy();
        }
    }

    owl.utils.whenReady().then(() => {
        const app = new AppowlComponent();
        app.mount(document.body);
    });
});