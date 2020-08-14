import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { EmbraceService } from './embrace.service';

@Component({
  selector: 'app-embrace',
  templateUrl: './embrace.component.html',
  styleUrls: ['./embrace.component.scss']
})
export class EmbraceComponent implements OnInit {
  submitOffenseForm;
  isValid = true;
  message: string;

  constructor(private embraceService: EmbraceService) {
    this.initialize();
  }

  initialize() {
    this.submitOffenseForm = new FormGroup({
      chargeCount: new FormControl(),
      isChargeDisposition: new FormControl('NONE'),
      offenseCategory: new FormControl(),
      isPrimaryCharge: new FormControl('NONE'),
      offenseTitle: new FormControl(),
      chargedClass: new FormControl(),
      sentenceJudge: new FormControl(),
      sentencePhase: new FormControl(),
      commitmentTerm: new FormControl(),
      commitmentUnit: new FormControl(),
      lengthOfCase: new FormControl(),
      ageAtIncident: new FormControl(),
      race: new FormControl(),
      gender: new FormControl(),
      incidentCity: new FormControl(),
      lawEnforcementAgency: new FormControl(),
      lawEnforcementUnit: new FormControl(),
      sentenceType: new FormControl()
    });
    this.isValid = true;
  }

  ngOnInit() {
  }

  onSubmit() {
    this.isValid = this.validateData(this.submitOffenseForm.value);
    if (!this.isValid) {
      this.message = 'All the fields are required. Please enter the valid information and submit again.';
    } else {
      this.message = undefined;

      if (this.submitOffenseForm.value.isChargeDisposition.toLowerCase() === 'true') {
        this.submitOffenseForm.value.isChargeDisposition = true;
      } else {
        this.submitOffenseForm.value.isChargeDisposition = false;
      }
      if (this.submitOffenseForm.value.isPrimaryCharge.toLowerCase() === 'true') {
        this.submitOffenseForm.value.isPrimaryCharge = true;
      } else {
        this.submitOffenseForm.value.isPrimaryCharge = false;
      }
      this.embraceService.submitData(this.submitOffenseForm.value)
        .subscribe((data: any) =>  {
          if (data && data.success) {
            this.isValid = true;
            this.message = data.message ? data.message : 'Close Order request submitted successfully.';
            this.initialize();
          } else {
            this.isValid = false;
            this.message = data.message ? data.message : 'Error occurred while submitting the request.';
          }
        });
    }
  }

  validateData(formData): boolean {
    if (
      !formData ||
      !formData.documentId ||
      !formData.isSuccess ||
      formData.isSuccess === 'NONE' ||
      !formData.description
    ) {
      return false;
    }
    return true;
  }
}
