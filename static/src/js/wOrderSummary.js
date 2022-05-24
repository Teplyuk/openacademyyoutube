
 // intro_to_owl_part_1.PartnerOrderSummary     ==> w1OrderSummary
 // PartnerOrderSummary                         ==> OrderSummary
 // partner                                     ==> youtube

//return this._rpc({
//                model: this.model,
//                method: 'activity_send_mail',
//                args: [[this.res_id], templateID],
//            })
//            .then(this._reload.bind(this, {activity: true, thread: true, followers: true}));
//    },

 odoo.define("w1OrderSummary", function (require) {

     const FormRenderer = require("web.FormRenderer");
     const { Component } = owl;
     const { ComponentWrapper } = require("web.OwlCompatibility");
     const { useState } = owl.hooks;

     class OrderSummary extends Component {
        partner = useState({});

        constructor(self, partner) {
            super();
            this.partner = partner;
            console.log('Hello Javascript1')
        }
     }

     /* Register properties to our widget. */
     Object.assign(OrderSummary, {template: "w1OrderSummary"});

     FormRenderer.include({
     async _renderView() {
         await this._super(...arguments);

         for(const element of this.el.querySelectorAll(".o_partner_order_summary")) {
             console.log('Hello Javascript2')
             console.log(this)
             this._rpc({
                 model: "youtube.patient",
                 method: "read",
                 args: [[this.state.data.id]]
             }).then(data => {
                 (new ComponentWrapper(
                     this,
                     OrderSummary,
                     useState(data[0])
                 )).mount(element);
             });
         }
     }
     });

//    model: "res.partner",
//    method: "read",
//    args: [[this.state.data.partner_id.res_id]]


 });