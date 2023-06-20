import { LightningElement, api, wire, track } from 'lwc';
import { CloseActionScreenEvent } from 'lightning/actions';

export default class SyncDesignSummary extends LightningElement {
  @api recordId;

  handleClick(event) {
    
    var h = new Headers();
    h.append("Content-Type", "application/json");

    
    var req_options = {
      method: 'GET',
    };
    fetch("https://www.workato.com/webhooks/rest/35ac0faa-1623-45fe-830d-77b6bc35d89b/sync-design-summary", req_options)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));
    this.dispatchEvent(new CloseActionScreenEvent());
  }
  handleCancel(event) {
    this.dispatchEvent(new CloseActionScreenEvent());
  }
}