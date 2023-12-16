class Data{
    constructor() {
        this.SEXE = null;
        this.EDAT_1 = null;
        this.EDAT_Q = null;
        this.EDAT_G = null;
        this.DECADA = null;
        this.LLOC_NAIX = null;
        this.LLOC_NAIX_CCAA = null;
        this.LLOC_NAIX_REGIO = null;
        this.NACIONALITAT_G = null;
        this.NACIONALITAT_REGIO = null;
        this.NIV_EDUCA_esta = null;
        this.CODI_DISTRICTE_DEST = null;
        this.CODI_BARRI_DEST = null;
    }

    changeSexValue(sex){
        if (sex != 0){ this.SEXE = sex; }
        else{ this.SEXE = null; }
        console.log("sex:", this.SEXE);
    }

    changeEducationValue(education){
        if (education != 0){ this.NIV_EDUCA_esta = education; }
        else{ this.NIV_EDUCA_esta = null; }
    }

    changeAgeValue(age){
        if (age >= 0){
            if(age > 100){
            this.EDAT_1 = 101;
            this.EDAT_Q = 20;}
            else{
            this.EDAT_1 = age;
            this.EDAT_Q = Math.floor(age / 5);}
            if(age<16){
                this.EDAT_G = 0;}
            else if(age<25){
                this.EDAT_G = 1;}
            else if(age<40){
                this.EDAT_G = 2;}
            else if(age<65){
                this.EDAT_G = 3;}
            else{
                this.EDAT_G = 4;}
            var date = new Date();
            year_of_birth = date.getFullYear() - age; //S'hauria de millorar en futures implementacions
            dec_aux = year_of_birth - 1930  //Demanariem data de naixement en lloc de fer això
            if(dec_aux < 0){
                this.DECADA = 1;}
            else{
                this.DECADA = Math.floor(dec_aux % 10) + 2;}                
        }
        else{ 
            this.EDAT_1 = null;
            this.EDAT_Q = null;
            this.EDAT_G = null;
            this.DECADA = null;
        }
    }

    changeDistrictValue(district){
        if (district != 0){ this.CODI_DISTRICTE_DEST = district; }
        else{ this.CODI_DISTRICTE_DEST = null; }
        this.CODI_BARRI_DEST = null;
    }

    changeNeighborhoodValue(neighborhood){
        if (neighborhood != 0){ this.CODI_BARRI_DEST = neighborhood; }
        else{ this.CODI_BARRI_DEST = null; }        
    }
}