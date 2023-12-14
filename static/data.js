
class Data{
    constructor() {
        this.SEXE = null;
        this.EDAT_1 = null;
        this.EDAT_Q = null;
        this.EDAT_G = null;
        this.LLOC_NAIX = null;
        this.LLOC_NAIX_CCAA = null;
        this.LLOC_NAIX_REGIO = null;
        this.NACIONALITAT_G = null;
        this.NACIONALITAT_REGIO = null;
        this.NIV_EDUCA_esta = null;
    }

    changeSexValue(sex){
        if (sex != 0){ this.SEXE = sex; }
        else{ this.SEXE = null; }
    }

    changeEducationValue(education){
        if (education != 0){ this.NIV_EDUCA_esta = education; }
        else{ this.NIV_EDUCA_esta = null; }
    }

}


