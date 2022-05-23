
 // intro_to_owl_part_1.PartnerOrderSummary     ==> w1OrderSummary
 // PartnerOrderSummary                         ==> OrderSummary

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
        }
     }

     /**
      * Register properties to our widget.
      */
     Object.assign(OrderSummary, {
         template: "w1OrderSummary"
     });

     /**
      * Override the form renderer so that we can mount the component on render
      * to any div with the class o_partner_order_summary.
      */
     FormRenderer.include({
         async _render() {
             await this._super(...arguments);

             for(const element of this.el.querySelectorAll(".o_partner_order_summary")) {
                 (new ComponentWrapper(this, OrderSummary))
                     .mount(element)
             }
         }
     });
 });