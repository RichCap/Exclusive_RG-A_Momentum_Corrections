########################################################################################
#----------#        Central Detector Pi+ Phi Shift (As of 2-16-2024)        #----------#
########################################################################################
# This definition is included in 'Central_Detector_Sector_Definition' below
# Used to define the Phi Shift for the Pi+ Pion detected in the Central Detector
# Do not define 'pipPhi_Shift' before using this code as written
Central_Detector_PipPhi_Shift = """
double pipPhi_Shift = pipPhi + (5/(pip-0.05));
"""

########################################################################################
#----------#      Central Detector Sector Definition (As of 2-16-2024)      #----------#
########################################################################################
# This definition is included in 'Correction_Code_Full_In' and 'Correction_Code_Full_Out' below
# Used to define the Central Detector Sector for the Pi+ Pions
# Must have a defined value for 'pipPhi' and 'tempsec' before using this code as written
Central_Detector_Sector_Definition = "".join(["""
if(pipPhi < -25){pipPhi += 360;}
pipPhi += 25;""", str(Central_Detector_PipPhi_Shift), """
int tempsec = pipsec;
if(pipsec > 6){
    if((pipPhi_Shift > 0   && pipPhi_Shift <=  60) || (pipPhi_Shift > 360)){
        // Note: For best results, make sure to apply the following redefinition of pipPhi: if(pipsec == 7 && pipPhi > 200){pipPhi += -360;}
        tempsec = 7;
    }
    if( pipPhi_Shift > 60  && pipPhi_Shift <= 120 ){
        tempsec = 8;
    }
    if( pipPhi_Shift > 120 && pipPhi_Shift <= 180 ){
        tempsec = 9;
    }
    if( pipPhi_Shift > 180 && pipPhi_Shift <= 240 ){
        tempsec = 10;
    }
    if( pipPhi_Shift > 240 && pipPhi_Shift <= 300 ){
        tempsec = 11;
    }
    if( pipPhi_Shift > 300 && pipPhi_Shift <= 360 ){
        tempsec = 12;
    }
}"""])


###################################################################################
#----------#      Last updated Inbending Corrections on: 8-27-2024     #----------#
###################################################################################
Correction_Code_Full_In = "".join(["""

auto dppC = [&](float Px, float Py, float Pz, int sec, int ivec, int corEl, int corPip, int corPim, int corPro){
    
    // 'sec' Corresponds to the Forward Detector Sectors where the given particle is detected (6 total)
    // For particles detected in the Central Detector, set the value of 'sec' to be any number greater than 6 (this code will automatically reassign the values of this input to be consistent with the definitions used by the corrections)
    
    // ivec = 0 --> Electron Corrections
    // ivec = 1 --> Pi+ Corrections
    // ivec = 2 --> Pi- Corrections
    // ivec = 3 --> Proton Corrections

    // corEl ==> Gives the 'generation' of the electron correction
        // corEl == 0 --> No Correction
        // corEl == 1 --> Final Version of Corrections
        // corEl == 2 --> Modified/Extended Correction (using the Elastic Events - based of existing corrections)
        // corEl == 3 --> New Extended Correction (using the Elastic Events - created from uncorrected ∆P Plots)
        // corEl == 4 --> Old Pass2 Corrections (Incomplete)
        // corEl == 5 --> New Pass2 Corrections (Refinement)
        // corEl == 6 --> New (Fall 2018) Pass 2 Correction (w/Pion Energy Loss)

    // corPip ==> Gives the 'generation' of the π+ Pion correction
        // corPip == 0 --> No Correction
        // corPip == 1 --> Old Version of Corrections
        // corPip == 2 --> Final Version of Corrections (uses the wrong name   - is mmExF - same correction as corPip == 3)
        // corPip == 3 --> Final Version of Corrections (uses the correct name - is mmEF  - same correction as corPip == 2)
        // corPip == 4 --> New Pass2 Corrections (Incomplete)
        // corPip == 5 --> New Pass2 Corrections (refinement of corPip == 4  --- is split between two functions at p = 4 GeV)
        // corPip == 6 --> New (Fall 2018) Pass 2 Correction (w/Pion Energy Loss)

    // corPim ==> Gives the 'generation' of the π- Pion correction
        // corPim == 0 --> No Correction
        // corPim == 1 --> Nick's Quadratic Momentum, Quadratic Phi

    // corPro ==> Gives the 'generation' of the Proton correction
        // corPro == 0 --> No Correction
        // corPro == 1 --> Quad Momentum, Quad Phi
        // corPro == 2 --> Quad Momentum, NO Phi
        // corPro == 3 --> Linear Momentum, NO Phi

    // Momentum Magnitude
    double pp = sqrt(Px*Px + Py*Py + Pz*Pz);

    // Initializing the correction factor
    double dp = 0;

    // Defining Phi Angle
    double Phi = (180/3.1415926)*atan2(Py, Px);

    // Central Detector Corrections
    if(sec > 6){
        if(ivec == 1){
            // For Central Detector π+ Pions
            """, str(str(str(Central_Detector_Sector_Definition).replace("pipP", "P")).replace("pip-", "pp-")).replace("pipsec", "sec"), """
            sec = tempsec; // New Definition of Central Detector Sectors
            if(sec == 7 && Phi_Shift > 200){Phi_Shift += -360;}
            double phi = Phi_Shift - (sec - 7)*60 - 30;
            // Central Detector Corrections for the π+ Pion go here (not made yet)
            return dp/pp;
        }
        else{return dp/pp;} // Central Detector Sectors/Corrections are not yet set up for particles other than the π+ Pion
    }

    // (Initial) Shift of the Phi Angle (done to realign sectors whose data is separated when plotted from ±180˚)
    if(((sec == 4 || sec == 3) && Phi < 0) || (sec > 4 && Phi < 90)){
        Phi += 360;
    }

    // Getting Local Phi Angle
    double PhiLocal = Phi - (sec - 1)*60;

    // Applying Shift Functions to Phi Angles (local shifted phi = phi)
    double phi = PhiLocal;

    // For Electron Shift
    if(ivec == 0){
        phi = PhiLocal - 30/pp;
    }

    // For π+ Pion/Proton Shift
    if(ivec == 1 || ivec == 3){
        phi = PhiLocal + (32/(pp-0.05));
    }

    // For π- Pion Shift
    if(ivec == 2){
        phi = PhiLocal - (32/(pp-0.05));
    }


    ////////////////////////////////////////////////////////////////////////////////////////////////
    //===============//===============//     No Corrections     //===============//===============//
    ////////////////////////////////////////////////////////////////////////////////////////////////

    if(corEl == 0 && ivec == 0){ // No Electron Correction
        dp = 0;
        return dp/pp;
    }
    if(corPip == 0 && ivec == 1){ // No π+ Pion Correction
        dp = 0;
        return dp/pp;
    }
    if(corPim == 0 && ivec == 2){ // No π- Pion Correction
        dp = 0;
        return dp/pp;
    }
    if(corPro == 0 && ivec == 3){ // No Proton Correction
        dp = 0;
        return dp/pp;
    }

    //////////////////////////////////////////////////////////////////////////////////////////////////
    //==============//==============//     No Corrections (End)     //==============//==============//
    //////////////////////////////////////////////////////////////////////////////////////////////////


    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //==================================================================================================================================//
    //=======================//=======================//     Electron Corrections     //=======================//=======================//
    //==================================================================================================================================//
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    if(corEl != 0 && ivec == 0){
        if(sec == 1){
            dp = ((1.57e-06)*phi*phi + (5.021e-05)*phi + (-1.74089e-03))*pp*pp + ((-2.192e-05)*phi*phi + (-1.12528e-03)*phi + (0.0146476))*pp + ((8.504e-05)*phi*phi + (2.08012e-03)*phi + (-0.0122501));
        }
        if(sec == 2){
            dp = ((-3.98e-06)*phi*phi + (1.66e-05)*phi + (-1.55918e-03))*pp*pp + ((2.136e-05)*phi*phi + (-5.7373e-04)*phi + (0.0143591))*pp + ((2.4e-06)*phi*phi + (1.6656e-03)*phi + (-0.0218711));
        }
        if(sec == 3){
            dp = ((5.57e-06)*phi*phi + (2.3e-07)*phi + (-2.26999e-03))*pp*pp + ((-7.761e-05)*phi*phi + (4.1437e-04)*phi + (0.0152985))*pp + ((2.2542e-04)*phi*phi + (-9.442e-04)*phi + (-0.0231432));
        }
        if(sec == 4){
            dp = ((3.48e-06)*phi*phi + (2.166e-05)*phi + (-2.29e-04))*pp*pp + ((-2.758e-05)*phi*phi + (7.226e-05)*phi + (-3.38e-03))*pp + ((3.166e-05)*phi*phi + (6.93e-05)*phi + (0.04767));
        }
        if(sec == 5){
            dp = ((1.19e-06)*phi*phi + (-2.286e-05)*phi + (-1.6332e-04))*pp*pp + ((-1.05e-06)*phi*phi + (7.04e-05)*phi + (-5.0754e-03))*pp + ((-7.22e-06)*phi*phi + (4.1748e-04)*phi + (0.04441));
        }
        if(sec == 6){
            dp = ((-5.97e-06)*phi*phi + (-3.689e-05)*phi + (5.782e-05))*pp*pp + ((6.573e-05)*phi*phi + (2.1376e-04)*phi + (-9.54576e-03))*pp + ((-1.7732e-04)*phi*phi + (-8.62e-04)*phi + (0.0618975));
        }

        // Extended Refinement of corEl == 1
        if(corEl == 2){
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Corrected][Sector 1] is:
                dp = dp + ((-1.5543e-05)*phi*phi + (-6.1257e-05)*phi + (9.0385e-04))*pp*pp + ((1.8051e-04)*phi*phi + (9.0971e-04)*phi + (-0.010544))*pp + ((-4.7617e-04)*phi*phi + (-0.0029024)*phi + (0.02882));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Corrected][Sector 2] is:
                dp = dp + ((-1.0753e-07)*phi*phi + (-4.3441e-05)*phi + (-2.4143e-04))*pp*pp + ((-9.1649e-06)*phi*phi + (5.5094e-04)*phi + (0.0046169))*pp + ((5.7005e-05)*phi*phi + (-0.0014851)*phi + (-0.017753));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Corrected][Sector 3] is:
                dp = dp + ((-1.3656e-05)*phi*phi + (-6.3819e-06)*phi + (9.4242e-04))*pp*pp + ((1.5109e-04)*phi*phi + (-1.6847e-04)*phi + (-0.010423))*pp + ((-3.8962e-04)*phi*phi + (0.001198)*phi + (0.029035));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Corrected][Sector 4] is:
                dp = dp + ((-7.7030e-06)*phi*phi + (-2.2183e-05)*phi + (-3.2310e-04))*pp*pp + ((9.1683e-05)*phi*phi + (1.8863e-04)*phi + (0.0025154))*pp + ((-2.3756e-04)*phi*phi + (-2.8317e-04)*phi + (-0.0046244));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Corrected][Sector 5] is:
                dp = dp + ((-8.7306e-07)*phi*phi + (2.1699e-05)*phi + (-5.7166e-04))*pp*pp + ((7.4275e-06)*phi*phi + (-2.5637e-04)*phi + (0.0054676))*pp + ((-1.2134e-05)*phi*phi + (8.1743e-04)*phi + (-0.010263));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Corrected][Sector 6] is:
                dp = dp + ((4.3560e-06)*phi*phi + (3.3573e-05)*phi + (-6.6964e-04))*pp*pp + ((-6.6393e-05)*phi*phi + (-3.0575e-04)*phi + (0.0084299))*pp + ((2.4042e-04)*phi*phi + (5.1189e-04)*phi + (-0.024095));
            }
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Corrected (Extended)][Sector 1] is:
                dp = dp + ((7.9660e-06)*phi*phi + (5.1523e-05)*phi + (-2.1894e-04))*pp*pp + ((-1.2252e-04)*phi*phi + (-6.2769e-04)*phi + (0.0029742))*pp + ((4.1380e-04)*phi*phi + (0.0017672)*phi + (-0.0092031));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Corrected (Extended)][Sector 2] is:
                dp = dp + ((-2.1372e-06)*phi*phi + (2.0673e-05)*phi + (-1.7416e-04))*pp*pp + ((2.0227e-05)*phi*phi + (-2.6449e-04)*phi + (0.0026238))*pp + ((-4.7051e-05)*phi*phi + (7.5652e-04)*phi + (-0.0086124));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Corrected (Extended)][Sector 3] is:
                dp = dp + ((3.3352e-09)*phi*phi + (-2.7138e-05)*phi + (1.8147e-04))*pp*pp + ((-2.2826e-05)*phi*phi + (2.6561e-04)*phi + (-0.0021432))*pp + ((1.3156e-04)*phi*phi + (-6.2599e-04)*phi + (0.0056483));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Corrected (Extended)][Sector 4] is:
                dp = dp + ((8.0009e-06)*phi*phi + (1.1847e-05)*phi + (-4.0825e-04))*pp*pp + ((-1.0793e-04)*phi*phi + (-1.8450e-04)*phi + (0.005087))*pp + ((3.2556e-04)*phi*phi + (5.9843e-04)*phi + (-0.014079));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Corrected (Extended)][Sector 5] is:
                dp = dp + ((3.5908e-07)*phi*phi + (-1.2954e-06)*phi + (-4.4109e-05))*pp*pp + ((-9.7218e-07)*phi*phi + (1.4249e-05)*phi + (2.9679e-04))*pp + ((-9.7975e-06)*phi*phi + (-5.2075e-05)*phi + (8.0729e-05));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Corrected (Extended)][Sector 6] is:
                dp = dp + ((-5.9006e-06)*phi*phi + (8.0310e-06)*phi + (2.0305e-04))*pp*pp + ((8.3625e-05)*phi*phi + (-4.1055e-05)*phi + (-0.0020693))*pp + ((-2.8471e-04)*phi*phi + (-6.3169e-05)*phi + (0.0046844));
            }
        }

        // New Corrections created from corEl == 0 (wider kinematic range than what was used to create corEl == 1)
        if(corEl == 3){
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Uncorrected][Sector 1] is:
                dp = ((-4.3303e-06)*phi*phi + (1.1006e-04)*phi + (-5.7235e-04))*pp*pp + ((3.2555e-05)*phi*phi + (-0.0014559)*phi + (0.0014878))*pp + ((-1.9577e-05)*phi*phi + (0.0017996)*phi + (0.025963));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Uncorrected][Sector 2] is:
                dp = ((-9.8045e-07)*phi*phi + (6.7395e-05)*phi + (-4.6757e-05))*pp*pp + ((-1.4958e-05)*phi*phi + (-0.0011191)*phi + (-0.0025143))*pp + ((1.2699e-04)*phi*phi + (0.0033121)*phi + (0.020819));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Uncorrected][Sector 3] is:
                dp = ((-5.9459e-07)*phi*phi + (-2.8289e-05)*phi + (-4.3541e-04))*pp*pp + ((-1.5025e-05)*phi*phi + (5.7730e-04)*phi + (-0.0077582))*pp + ((7.3348e-05)*phi*phi + (-0.001102)*phi + (0.057052));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Uncorrected][Sector 4] is:
                dp = ((-2.2714e-06)*phi*phi + (-3.0360e-05)*phi + (-8.9322e-04))*pp*pp + ((2.9737e-05)*phi*phi + (5.1142e-04)*phi + (0.0045641))*pp + ((-1.0582e-04)*phi*phi + (-5.6852e-04)*phi + (0.027506));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Uncorrected][Sector 5] is:
                dp = ((-1.1490e-06)*phi*phi + (-6.2147e-06)*phi + (-4.7235e-04))*pp*pp + ((3.7039e-06)*phi*phi + (-1.5943e-04)*phi + (-8.5238e-04))*pp + ((4.4069e-05)*phi*phi + (0.0014152)*phi + (0.031933));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Uncorrected][Sector 6] is:
                dp = ((1.1076e-06)*phi*phi + (4.0156e-05)*phi + (-1.6341e-04))*pp*pp + ((-2.8613e-05)*phi*phi + (-5.1861e-04)*phi + (-0.0056437))*pp + ((1.2419e-04)*phi*phi + (4.9084e-04)*phi + (0.049976));
            }
        }

        // Spring 2019 - Pass 2 Corrections
        if(corEl == 4 || corEl == 5){ // Pass 2 Corrections (i.e., 'mmP2' and 'mmRP2')
            if(sec == 1){
                dp = (-4.3927e-04)*pp*pp + (5.8658e-04)*pp + (0.02801);
            }
            if(sec == 2){
                dp = (4.8839e-04)*pp*pp + (-0.01132)*pp + (0.05124);
            }
            if(sec == 3){
                dp = (3.3571e-04)*pp*pp + (-0.01172)*pp + (0.05763);
            }
            if(sec == 4){
                dp = (1.0268e-04)*pp*pp + (-4.8374e-03)*pp + (0.0412);
            }
            if(sec == 5){
                dp = (2.8250e-04)*pp*pp + (-7.9847e-03)*pp + (0.04232);
            }
            if(sec == 6){
                dp = (1.3589e-04)*pp*pp + (-6.7704e-03)*pp + (0.03464);
            }

            if(corEl == 5){ // Phi-dependent Refinement of Pass 2 Corrections
                if(sec == 1){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmP2          (Pass 2 Correction)][Sector 1] is:
                    dp = dp +  ((1.0461e-07)*phi*phi +  (2.0228e-05)*phi +  (1.7357e-04))*pp*pp + ((-8.7646e-06)*phi*phi + (-3.9387e-04)*phi + (-5.4988e-04))*pp +  ((6.0164e-05)*phi*phi +   (0.0010708)*phi + (-0.0030032));
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 1] is:
                    dp = dp + ((-6.4421e-07)*phi*phi + (-1.3073e-05)*phi + (-1.4102e-05))*pp*pp +  ((6.7547e-06)*phi*phi +  (1.0047e-04)*phi +  (3.1341e-04))*pp + ((-1.6767e-05)*phi*phi + (-2.0917e-04)*phi + (-0.0013211));
                }
                if(sec == 2){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmP2          (Pass 2 Correction)][Sector 2] is:
                    dp = dp + ((-7.3200e-07)*phi*phi +  (2.5209e-05)*phi + (-3.7645e-04))*pp*pp + ((-6.7578e-07)*phi*phi + (-5.1042e-04)*phi +   (0.0049163))*pp +  ((3.4087e-05)*phi*phi +   (0.0018198)*phi +  (-0.014044));
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 2] is:
                    dp = dp + ((-7.4037e-07)*phi*phi + (-1.4694e-05)*phi + (-5.5340e-05))*pp*pp +  ((7.4548e-06)*phi*phi +  (1.2889e-04)*phi +  (6.2012e-04))*pp + ((-1.7841e-05)*phi*phi + (-2.6237e-04)*phi + (-0.0017847));
                }
                if(sec == 3){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmP2          (Pass 2 Correction)][Sector 3] is:
                    dp = dp + ((-4.3080e-08)*phi*phi +  (1.9303e-05)*phi + (-2.7301e-04))*pp*pp + ((-5.8015e-06)*phi*phi + (-1.8028e-04)*phi +   (0.0036556))*pp +  ((3.7849e-05)*phi*phi +  (4.8794e-04)*phi +  (-0.010733));
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 3] is:
                    dp = dp + ((-7.7040e-07)*phi*phi +  (9.8938e-06)*phi + (-7.6219e-05))*pp*pp +  ((6.0610e-06)*phi*phi + (-8.0530e-05)*phi +   (0.0010106))*pp + ((-8.5135e-06)*phi*phi +  (1.5472e-04)*phi + (-0.0031448));
                }
                if(sec == 4){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmP2          (Pass 2 Correction)][Sector 4] is:
                    dp = dp + ((-4.1853e-07)*phi*phi +  (1.0473e-05)*phi + (-6.5274e-05))*pp*pp +  ((3.6816e-06)*phi*phi + (-1.5587e-05)*phi +  (7.6000e-04))*pp + ((-7.1764e-06)*phi*phi + (-1.5987e-04)*phi + (-0.0020378));
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 4] is:
                    dp = dp + ((-3.2135e-07)*phi*phi +  (2.7994e-06)*phi +  (4.7069e-05))*pp*pp + ((-3.3353e-07)*phi*phi + (-1.2275e-05)*phi + (-4.2176e-04))*pp +  ((1.0466e-05)*phi*phi +  (2.0954e-05)*phi + (8.1115e-04));
                }
                if(sec == 5){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmP2          (Pass 2 Correction)][Sector 5] is:
                    dp = dp +  ((1.1760e-06)*phi*phi +  (2.9355e-05)*phi + (-2.1403e-04))*pp*pp + ((-1.8923e-05)*phi*phi + (-4.2933e-04)*phi +     (0.00421))*pp +  ((7.2838e-05)*phi*phi +   (0.0012461)*phi +  (-0.014348));
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 5] is:
                    dp = dp + ((-1.5632e-06)*phi*phi + (-7.1527e-06)*phi +  (9.9895e-05))*pp*pp +  ((1.8332e-05)*phi*phi +  (5.5202e-05)*phi + (-0.0012584))*pp +  ((-5.1594e-05)*phi*phi + (-1.0622e-04)*phi +  (0.0036533));
                }
                if(sec == 6){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmP2          (Pass 2 Correction)][Sector 6] is:
                    dp = dp + ((-7.4655e-07)*phi*phi + (-3.2506e-05)*phi +  (3.0801e-04))*pp*pp +  ((3.7179e-07)*phi*phi +  (3.3195e-04)*phi +  (-0.0015145))*pp +  ((4.6216e-05)*phi*phi + (-7.6947e-04)*phi +  (-0.001801));
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 6] is:
                    dp = dp + ((-9.7434e-07)*phi*phi + (-6.4726e-06)*phi + (-6.1383e-05))*pp*pp +  ((1.1760e-05)*phi*phi +  (5.5914e-05)*phi +  (8.6014e-04))*pp + ((-3.4082e-05)*phi*phi + (-1.0690e-04)*phi + (-0.0027697));
                }
                
                // Refinements made after fixing the exclusivity cuts - Cuts were from fits of the 1.75*sigma (upper) and 2*sigma (lower) widths of the Missing/Invariant Mass distributions as functions of the electron momentum/sector/non-continuous phi (no phi for the elastic scattering cuts) - 1st ran with Extra_Version_Name = "_V10" (made with Extra_Version_Name = "_V9")
                if(sec == 1){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 1] is:
                    dp = dp + ((-1.1292e-06)*phi*phi + (-2.3124e-06)*phi + (-7.6258e-05))*pp*pp + ((1.9090e-05)*phi*phi + (-3.5616e-05)*phi + (7.3079e-04))*pp + ((-7.3456e-05)*phi*phi + (6.8312e-04)*phi + (-2.9655e-04));
                }
                if(sec == 2){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 2] is:
                    dp = dp + ((-1.4231e-06)*phi*phi + (-1.5868e-05)*phi + (1.9364e-04))*pp*pp + ((1.6746e-05)*phi*phi + (1.5182e-04)*phi + (-0.0030687))*pp + ((-4.5275e-05)*phi*phi + (-2.1582e-04)*phi + (0.0117));
                }
                if(sec == 3){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 3] is:
                    dp = dp + ((-3.2233e-06)*phi*phi + (-2.7358e-05)*phi + (-3.8901e-05))*pp*pp + ((3.3948e-05)*phi*phi + (3.3560e-04)*phi + (0.0011806))*pp + ((-8.6514e-05)*phi*phi + (-0.0010091)*phi + (-0.0050875));
                }
                if(sec == 4){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 4] is:
                    dp = dp + ((-1.0316e-06)*phi*phi + (-1.6299e-05)*phi + (1.1550e-04))*pp*pp + ((1.6063e-05)*phi*phi + (2.7983e-04)*phi + (-0.0012447))*pp + ((-6.6546e-05)*phi*phi + (-0.0011668)*phi + (0.0028535));
                }
                if(sec == 5){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 5] is:
                    dp = dp + ((-1.0044e-06)*phi*phi + (-5.2491e-07)*phi + (4.0706e-05))*pp*pp + ((1.3242e-05)*phi*phi + (2.5438e-05)*phi + (-6.5783e-04))*pp + ((-4.3946e-05)*phi*phi + (-2.8484e-04)*phi + (0.0041747));
                }
                if(sec == 6){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 6] is:
                    dp = dp + ((-2.2626e-07)*phi*phi + (-8.5683e-06)*phi + (-9.6293e-05))*pp*pp + ((2.4282e-08)*phi*phi + (5.5672e-05)*phi + (0.0017293))*pp + ((8.8971e-06)*phi*phi + (1.5514e-04)*phi + (-0.0073817));
                }

                // Refinements made from Extra_Version_Name = "_V10" for Extra_Version_Name = "_V11" 
                if(sec == 1){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 1] is:
                    dp = dp + ((5.0040e-08)*phi*phi + (-8.0456e-07)*phi + (3.3400e-05))*pp*pp + ((-9.3404e-07)*phi*phi + (1.4125e-05)*phi + (-4.8204e-04))*pp + ((3.2155e-06)*phi*phi + (-1.9460e-05)*phi + (0.0017124));
                }
                if(sec == 2){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 2] is:
                    dp = dp + ((-6.7044e-07)*phi*phi + (2.8531e-06)*phi + (2.3486e-05))*pp*pp + ((6.4134e-06)*phi*phi + (-2.8246e-05)*phi + (-3.0853e-04))*pp + ((-1.2267e-05)*phi*phi + (5.9773e-05)*phi + (9.1883e-04));
                }
                if(sec == 3){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 3] is:
                    dp = dp + ((-1.1237e-06)*phi*phi + (-3.3308e-06)*phi + (-1.1274e-05))*pp*pp + ((9.5363e-06)*phi*phi + (1.9525e-05)*phi + (9.1049e-05))*pp + ((-1.6966e-05)*phi*phi + (-3.0262e-05)*phi + (-2.5634e-04));
                }
                if(sec == 4){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 4] is:
                    dp = dp + ((2.5857e-06)*phi*phi + (9.3712e-06)*phi + (-3.2810e-04))*pp*pp + ((-2.8798e-05)*phi*phi + (-1.2463e-04)*phi + (0.0034551))*pp + ((6.1470e-05)*phi*phi + (3.7680e-04)*phi + (-0.0067891));
                }
                if(sec == 5){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 5] is:
                    dp = dp + ((-2.3158e-07)*phi*phi + (1.4747e-06)*phi + (4.3914e-05))*pp*pp + ((1.7677e-07)*phi*phi + (-1.6546e-05)*phi + (-3.7718e-04))*pp + ((8.4806e-06)*phi*phi + (2.7950e-05)*phi + (4.4451e-04));
                }
                if(sec == 6){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 6] is:
                    dp = dp + ((-1.6987e-06)*phi*phi + (-2.5568e-06)*phi + (1.7701e-04))*pp*pp + ((2.1510e-05)*phi*phi + (2.9852e-05)*phi + (-0.0022824))*pp + ((-6.5180e-05)*phi*phi + (-7.1982e-05)*phi + (0.0068033));
                }
                
                
                // Electron Refinement made from Extra_Version_Name = "Spring_2019_Pass_2_rec_clas_V11" (Turned off existing pion corrections - Made on 8/27/2024)
                if(sec == 1){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2][Sector 1] is:
                    dp = dp + ((-1.5651e-06)*phi*phi +  (2.1385e-06)*phi +  (5.0374e-04))*pp*pp +  ((1.8010e-05)*phi*phi + (-3.1024e-05)*phi +  (-0.005365))*pp + ((-4.8259e-05)*phi*phi +  (1.4741e-04)*phi +  (0.012994));
                }
                if(sec == 2){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2][Sector 2] is:
                    dp = dp + ((-9.1108e-07)*phi*phi + (-3.0003e-05)*phi +  (2.3554e-04))*pp*pp +  ((1.1558e-05)*phi*phi +  (3.3590e-04)*phi + (-0.0025058))*pp + ((-3.0431e-05)*phi*phi + (-7.8965e-04)*phi +  (0.0067678));
                }
                if(sec == 3){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2][Sector 3] is:
                    dp = dp +  ((1.5934e-08)*phi*phi +  (1.8340e-05)*phi +  (3.5219e-04))*pp*pp + ((-4.5515e-06)*phi*phi + (-2.2195e-04)*phi + (-0.0034717))*pp +  ((1.9827e-05)*phi*phi +  (6.2840e-04)*phi +  (0.0081064));
                }
                if(sec == 4){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2][Sector 4] is:
                    dp = dp +  ((6.2324e-07)*phi*phi +  (1.1346e-05)*phi +  (3.6653e-04))*pp*pp + ((-7.3528e-06)*phi*phi + (-1.4752e-04)*phi + (-0.0039926))*pp +  ((2.7790e-05)*phi*phi +  (4.7698e-04)*phi +  (0.0088635));
                }
                if(sec == 5){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2][Sector 5] is:
                    dp = dp + ((-5.1262e-06)*phi*phi + (-1.1644e-05)*phi +   (0.0010941))*pp*pp +  ((6.6509e-05)*phi*phi +  (1.2888e-04)*phi +  (-0.013983))*pp + ((-2.1289e-04)*phi*phi + (-2.6711e-04)*phi +  (0.044208));
                }
                if(sec == 6){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2][Sector 6] is:
                    dp = dp +  ((1.1942e-06)*phi*phi + (-2.1371e-08)*phi +  (4.8717e-04))*pp*pp + ((-2.0233e-05)*phi*phi +  (3.0953e-05)*phi + (-0.0053122))*pp +  ((8.0251e-05)*phi*phi + (-2.2055e-04)*phi +  (0.013047));
                }
                
            }
        }
        
        
        // Fall 2018 - Pass 2 Corrections
        if(corEl == 6){
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mm0_ELPipMM0][Sector 1] is:
                dp =      ((-2.9814e-06)*phi*phi + (-1.3177e-06)*phi + (-3.9424e-04))*pp*pp +  ((3.1475e-05)*phi*phi + (-1.7967e-04)*phi +  (3.7474e-04))*pp + ((-6.5941e-05)*phi*phi +  (8.3099e-04)*phi + (0.032777));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mm0_ELPipMM0][Sector 2] is:
                dp =      ((-9.1199e-08)*phi*phi +  (1.5504e-05)*phi + (-8.6526e-04))*pp*pp + ((-1.4237e-05)*phi*phi + (-3.8364e-04)*phi +   (0.0065896))*pp +  ((9.4995e-05)*phi*phi +   (0.0013291)*phi + (-0.0014618));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mm0_ELPipMM0][Sector 3] is:
                dp =      ((-1.7128e-06)*phi*phi +  (3.6506e-05)*phi + (-5.0322e-04))*pp*pp +  ((1.1945e-05)*phi*phi + (-4.3094e-04)*phi +   (0.0025542))*pp +  ((6.9253e-06)*phi*phi +  (9.8027e-04)*phi + (0.0062225));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mm0_ELPipMM0][Sector 4] is:
                dp =      ((-3.4682e-06)*phi*phi +  (2.2003e-05)*phi +  (5.7129e-04))*pp*pp +  ((4.1493e-05)*phi*phi + (-1.4497e-04)*phi +   (-0.010517))*pp + ((-1.0323e-04)*phi*phi + (-2.7535e-04)*phi + (0.062998));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mm0_ELPipMM0][Sector 5] is:
                dp =       ((8.6648e-07)*phi*phi +  (2.5573e-05)*phi +  (6.5377e-05))*pp*pp + ((-1.0315e-05)*phi*phi + (-3.5840e-04)*phi +  (-0.0066741))*pp +  ((2.1142e-05)*phi*phi +  (5.8774e-04)*phi + (0.045555));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mm0_ELPipMM0][Sector 6] is:
                dp =       ((2.2827e-06)*phi*phi + (-8.3888e-06)*phi + (-3.2263e-04))*pp*pp + ((-3.6229e-05)*phi*phi +  (1.2242e-04)*phi + (-4.8752e-04))*pp +  ((1.4049e-04)*phi*phi + (-5.0717e-04)*phi + (0.021858));
            }
            
            // Refinement made from Extra_Version_Name = "Forward_Fall2018_P2_Test_V2"
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMM0][Sector 1] is:
                dp = dp +  ((2.1054e-07)*phi*phi + (-2.2491e-05)*phi + (-8.5798e-05))*pp*pp + ((-7.1256e-06)*phi*phi +  (1.9323e-04)*phi +   (0.0014213))*pp +  ((3.4079e-05)*phi*phi + (-3.7406e-04)*phi + (-0.0050973));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMM0][Sector 2] is:
                dp = dp + ((-2.6120e-06)*phi*phi + (-1.7473e-05)*phi + (-4.4569e-05))*pp*pp +  ((3.0510e-05)*phi*phi +  (1.6557e-04)*phi +  (3.7791e-04))*pp + ((-8.3982e-05)*phi*phi + (-3.9073e-04)*phi + (-7.4750e-04));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMM0][Sector 3] is:
                dp = dp + ((-1.2384e-08)*phi*phi + (-1.2878e-05)*phi + (-1.5680e-04))*pp*pp + ((-7.6080e-06)*phi*phi +  (2.0174e-04)*phi +   (0.0022586))*pp +  ((4.8887e-05)*phi*phi + (-7.6605e-04)*phi + (-0.0076052));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMM0][Sector 4] is:
                dp = dp +  ((1.1756e-06)*phi*phi +  (9.2843e-06)*phi + (-3.8049e-04))*pp*pp + ((-1.5805e-05)*phi*phi + (-6.8510e-05)*phi +   (0.0039821))*pp +  ((3.5444e-05)*phi*phi + (-1.3072e-04)*phi + (-0.0052522));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMM0][Sector 5] is:
                dp = dp +  ((1.3520e-06)*phi*phi + (-2.2701e-06)*phi + (-1.4880e-04))*pp*pp + ((-1.7672e-05)*phi*phi + (-7.3631e-06)*phi +   (0.0018864))*pp +  ((5.2958e-05)*phi*phi +  (4.8608e-05)*phi + (-0.005351));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMM0][Sector 6] is:
                dp = dp + ((-2.1844e-06)*phi*phi + (-4.4769e-06)*phi + (-3.0654e-05))*pp*pp +  ((2.6552e-05)*phi*phi +  (1.8092e-05)*phi +  (5.2104e-04))*pp + ((-7.6253e-05)*phi*phi +  (5.1816e-05)*phi + (-0.001956));
            }
            
            // Refinement made from Extra_Version_Name = "Forward_Fall2018_P2_Test_V3"
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMM0][Sector 1] is:
                dp = dp + ((-4.4455e-06)*phi*phi +  (5.2006e-06)*phi +  (5.2186e-04))*pp*pp +  ((5.4746e-05)*phi*phi + (-1.0079e-04)*phi +  (-0.0069383))*pp + ((-1.5578e-04)*phi*phi +  (3.5947e-04)*phi + (0.024074));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMM0][Sector 2] is:
                dp = dp + ((-5.0891e-06)*phi*phi + (-2.0499e-05)*phi +  (3.3179e-04))*pp*pp +  ((6.1969e-05)*phi*phi +  (2.2982e-04)*phi +  (-0.0046372))*pp + ((-1.7498e-04)*phi*phi + (-5.9972e-04)*phi + (0.018597));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMM0][Sector 3] is:
                dp = dp + ((-3.9399e-06)*phi*phi + (-1.1728e-05)*phi + (-1.7596e-04))*pp*pp +  ((4.7853e-05)*phi*phi +  (1.5792e-04)*phi +   (0.0016687))*pp + ((-1.4504e-04)*phi*phi + (-4.8236e-04)*phi + (0.0016249));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMM0][Sector 4] is:
                dp = dp + ((-9.1117e-09)*phi*phi +  (1.2690e-05)*phi + (-3.6216e-04))*pp*pp + ((-1.4697e-06)*phi*phi + (-1.7092e-04)*phi +   (0.0044829))*pp +  ((1.7339e-05)*phi*phi +  (6.4128e-04)*phi + (-0.010911));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMM0][Sector 5] is:
                dp = dp + ((-1.6660e-06)*phi*phi +  (1.2066e-05)*phi +  (2.5740e-04))*pp*pp +  ((2.1087e-05)*phi*phi + (-2.2948e-04)*phi +  (-0.0034624))*pp + ((-6.1307e-05)*phi*phi +  (8.9383e-04)*phi + (0.014613));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMM0][Sector 6] is:
                dp = dp + ((-1.9016e-06)*phi*phi +  (1.2110e-05)*phi +  (2.6684e-04))*pp*pp +  ((2.4525e-05)*phi*phi + (-1.1772e-04)*phi +  (-0.0034957))*pp + ((-7.8749e-05)*phi*phi +  (2.3031e-04)*phi + (0.015083));
            }
            
            
            // Refinement made from Extra_Version_Name = "Forward_Fall2018_P2_Test_V7"
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMMfaP2][Sector 1] is:
                dp = dp + ((-2.6078e-06)*phi*phi + (-4.3875e-06)*phi + (2.5482e-04))*pp*pp + ((3.2246e-05)*phi*phi + (6.6817e-05)*phi + (-0.00348))*pp + ((-9.4096e-05)*phi*phi + (-2.2928e-04)*phi + (0.01352));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMMfaP2][Sector 2] is:
                dp = dp + ((5.0347e-08)*phi*phi + (6.5833e-08)*phi + (1.5151e-04))*pp*pp + ((-2.8341e-06)*phi*phi + (-2.5084e-05)*phi + (-0.0020883))*pp + ((1.6091e-05)*phi*phi + (2.4040e-04)*phi + (0.0089674));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMMfaP2][Sector 3] is:
                dp = dp + ((5.4972e-07)*phi*phi + (-2.3883e-05)*phi + (1.5269e-04))*pp*pp + ((-6.9613e-06)*phi*phi + (2.7983e-04)*phi + (-0.0029828))*pp + ((-1.2184e-06)*phi*phi + (-7.9843e-04)*phi + (0.017712));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMMfaP2][Sector 4] is:
                dp = dp + ((-1.6261e-06)*phi*phi + (-2.1688e-05)*phi + (2.9801e-04))*pp*pp + ((2.4431e-05)*phi*phi + (2.5886e-04)*phi + (-0.0039035))*pp + ((-9.5725e-05)*phi*phi + (-5.2092e-04)*phi + (0.013865));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMMfaP2][Sector 5] is:
                dp = dp + ((2.5118e-07)*phi*phi + (-9.5617e-06)*phi + (1.8624e-04))*pp*pp + ((-3.0324e-06)*phi*phi + (7.8390e-05)*phi + (-0.0026539))*pp + ((5.7233e-06)*phi*phi + (2.6912e-05)*phi + (0.011676));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMMfaP2][Sector 6] is:
                dp = dp + ((-1.5191e-07)*phi*phi + (8.7979e-06)*phi + (6.5120e-05))*pp*pp + ((2.1214e-06)*phi*phi + (-8.5858e-05)*phi + (-0.0013935))*pp + ((-1.3211e-05)*phi*phi + (1.5676e-04)*phi + (0.0097685));
            }
            
            
            // Split Electron Refinement made from Extra_Version_Name = "Forward_Fall2018_P2_Test_V9" (no Pion Momentum or Energy Loss Corrections were used) - Made on 8/21/2024
            if(pp < 7){
                if(sec == 1){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 1] is:
                    dp = dp + ((-3.4001e-06)*phi*phi + (-2.2885e-05)*phi +  (9.9705e-04))*pp*pp +  ((2.1840e-05)*phi*phi +  (2.4238e-04)*phi + (-0.0091904))*pp + ((-2.9180e-05)*phi*phi + (-6.4496e-04)*phi +  (0.022505));
                }
                if(sec == 2){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 2] is:
                    dp = dp +  ((5.3611e-06)*phi*phi +  (8.1979e-06)*phi +  (5.9789e-04))*pp*pp + ((-4.8185e-05)*phi*phi + (-1.5188e-04)*phi + (-0.0084675))*pp +  ((9.2324e-05)*phi*phi +  (6.4420e-04)*phi +  (0.026792));
                }
                if(sec == 3){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 3] is:
                    dp = dp +  ((9.9281e-07)*phi*phi +  (3.4879e-06)*phi +   (0.0011673))*pp*pp + ((-2.0071e-05)*phi*phi + (-3.1362e-05)*phi +  (-0.012329))*pp +  ((6.9463e-05)*phi*phi +  (3.5102e-05)*phi +  (0.037505));
                }
                if(sec == 4){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 4] is:
                    dp = dp + ((-4.8455e-06)*phi*phi + (-1.2074e-05)*phi +   (0.0013221))*pp*pp +  ((3.2207e-05)*phi*phi +  (1.3144e-04)*phi +  (-0.010451))*pp + ((-3.7365e-05)*phi*phi + (-4.2344e-04)*phi +  (0.019952));
                }
                if(sec == 5){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 5] is:
                    dp = dp +  ((7.7156e-07)*phi*phi + (-3.9566e-05)*phi + (-2.3589e-04))*pp*pp + ((-9.8309e-06)*phi*phi +  (3.7353e-04)*phi +  (0.0020382))*pp +  ((2.9506e-05)*phi*phi + (-8.0409e-04)*phi + (-0.0045615));
                }
                if(sec == 6){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 6] is:
                    dp = dp + ((-8.2535e-07)*phi*phi +  (9.1433e-06)*phi +  (3.5395e-04))*pp*pp + ((-3.4272e-06)*phi*phi + (-1.3012e-04)*phi + (-0.0030724))*pp +  ((4.9211e-05)*phi*phi +  (4.5807e-04)*phi +  (0.0058932));
                }
            }
            else{
                if(sec == 1){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 1] is:
                    dp = dp + ((-6.3656e-05)*phi*phi +  (1.7266e-04)*phi + (-0.0017909))*pp*pp +     ((0.00104)*phi*phi +   (-0.0028401)*phi +    (0.02981))*pp +  ((-0.0041995)*phi*phi +    (0.011537)*phi + (-0.1196));
                }
                if(sec == 2){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 2] is:
                    dp = dp + ((-6.1139e-05)*phi*phi +  (5.4087e-06)*phi + (-0.0021284))*pp*pp +   ((0.0010007)*phi*phi +   (9.3492e-05)*phi +   (0.039813))*pp +  ((-0.0040434)*phi*phi +  (-0.0010953)*phi + (-0.18112));
                }
                if(sec == 3){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 3] is:
                    dp = dp + ((-3.2178e-06)*phi*phi +  (4.0630e-05)*phi + (-0.005209))*pp*pp +   ((2.0884e-05)*phi*phi +  (-6.8800e-04)*phi +   (0.086513))*pp +  ((3.9530e-05)*phi*phi +   (0.0029306)*phi + (-0.3507));
                }
                if(sec == 4){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 4] is:
                    dp = dp + ((-3.9554e-05)*phi*phi +  (5.5496e-06)*phi + (-0.0058293))*pp*pp +  ((6.5077e-04)*phi*phi +   (2.6735e-05)*phi +   (0.095025))*pp +  ((-0.0026457)*phi*phi + (-6.1394e-04)*phi + (-0.3793));
                }
                if(sec == 5){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 5] is:
                    dp = dp + ((-3.2410e-05)*phi*phi + (-4.3301e-05)*phi + (-0.0028742))*pp*pp +  ((5.3787e-04)*phi*phi +   (6.8921e-04)*phi +   (0.049578))*pp +  ((-0.0021955)*phi*phi +  (-0.0027698)*phi + (-0.21142));
                }
                if(sec == 6){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 6] is:
                    dp = dp + ((-4.9760e-05)*phi*phi + (-7.2903e-05)*phi + (-0.0020453))*pp*pp +  ((8.0918e-04)*phi*phi +    (0.0011688)*phi +   (0.037042))*pp +  ((-0.0032504)*phi*phi +  (-0.0046169)*phi + (-0.16331));
                }
            }
            
            // Electron Refinement made from Extra_Version_Name = "Forward_Fall2018_P2_In_Refine_V1" (no Pion Momentum or Energy Loss Corrections were used) - Made on 8/21/2024
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 1] is:
                dp = dp + ((-1.9399e-06)*phi*phi + (-1.6333e-07)*phi +  (3.0018e-04))*pp*pp +  ((2.3684e-05)*phi*phi + (-2.4092e-06)*phi +  (-0.0039548))*pp + ((-6.5560e-05)*phi*phi +  (9.4533e-06)*phi +  (0.012199));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 2] is:
                dp = dp +  ((6.1358e-07)*phi*phi +  (2.5046e-06)*phi + (-1.1132e-04))*pp*pp + ((-1.1562e-05)*phi*phi + (-5.1391e-05)*phi +   (0.0011969))*pp +  ((5.2633e-05)*phi*phi +  (2.3068e-04)*phi + (-0.0030401));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 3] is:
                dp = dp + ((-2.1976e-06)*phi*phi +  (4.0238e-06)*phi +  (2.7167e-04))*pp*pp +  ((3.0279e-05)*phi*phi + (-2.7885e-05)*phi +   (-0.004621))*pp + ((-9.4739e-05)*phi*phi + (-4.5514e-05)*phi +  (0.018635));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 4] is:
                dp = dp + ((-4.5542e-07)*phi*phi +  (1.0199e-05)*phi +  (7.1880e-05))*pp*pp +  ((4.2848e-06)*phi*phi + (-1.3492e-04)*phi + (-9.2514e-04))*pp + ((-6.1931e-06)*phi*phi +  (3.8253e-04)*phi +  (0.0028805));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 5] is:
                dp = dp + ((-8.6861e-07)*phi*phi + (-4.7875e-06)*phi +  (2.3050e-05))*pp*pp +  ((1.0963e-05)*phi*phi +  (6.7035e-05)*phi + (-1.0457e-04))*pp + ((-3.1006e-05)*phi*phi + (-2.1679e-04)*phi +  (8.5870e-05));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 6] is:
                dp = dp + ((-2.0123e-06)*phi*phi +  (4.6879e-06)*phi +  (5.7260e-05))*pp*pp +  ((2.5903e-05)*phi*phi + (-1.6656e-05)*phi + (-6.5263e-04))*pp + ((-7.7379e-05)*phi*phi + (-6.1770e-05)*phi +  (0.0018685));
            }
            
            
            // Electron Refinement made from Extra_Version_Name = "Forward_Fall2018_P2_In_Refine_V2" (no Pion Momentum or Energy Loss Corrections were used) - Made on 8/22/2024
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 1] is:
                dp = dp +  ((2.2677e-06)*phi*phi +  (8.3417e-07)*phi + (-3.4408e-04))*pp*pp + ((-3.0915e-05)*phi*phi + (-2.1339e-05)*phi +   (0.0044457))*pp +  ((9.8413e-05)*phi*phi +  (8.6919e-05)*phi +   (-0.013349));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 2] is:
                dp = dp +  ((8.5417e-09)*phi*phi + (-5.4500e-07)*phi +  (1.3060e-05))*pp*pp + ((-1.2956e-06)*phi*phi +  (7.7321e-06)*phi +  (1.0652e-04))*pp +  ((5.4069e-06)*phi*phi + (-1.5292e-05)*phi +  (-0.0010013));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 3] is:
                dp = dp +  ((1.7930e-06)*phi*phi + (-5.3354e-06)*phi + (-2.3216e-04))*pp*pp + ((-2.4758e-05)*phi*phi +  (5.2322e-05)*phi +   (0.0029323))*pp +  ((8.3776e-05)*phi*phi + (-1.0643e-04)*phi +  (-0.0093214));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 4] is:
                dp = dp + ((-3.8889e-09)*phi*phi +  (3.8683e-06)*phi + (-4.9800e-06))*pp*pp + ((-2.6090e-07)*phi*phi + (-4.5943e-05)*phi +  (9.7920e-05))*pp +  ((1.0621e-06)*phi*phi +  (1.1495e-04)*phi + (-3.2819e-04));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 5] is:
                dp = dp + ((-3.4649e-07)*phi*phi + (-3.7212e-06)*phi +  (2.6630e-05))*pp*pp +  ((3.7368e-06)*phi*phi +  (4.8012e-05)*phi + (-2.8812e-04))*pp + ((-9.3626e-06)*phi*phi + (-1.5399e-04)*phi +  (6.5411e-04));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 6] is:
                dp = dp +  ((1.2970e-06)*phi*phi +  (1.1598e-05)*phi +  (2.4030e-05))*pp*pp + ((-1.8678e-05)*phi*phi + (-1.6229e-04)*phi + (-2.9591e-04))*pp +  ((6.4361e-05)*phi*phi +  (5.2820e-04)*phi +  (7.9658e-04));
            }
            
        }
        
    }


    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //====================================================================================================================================//
    //======================//======================//     Electron Corrections (End)     //======================//======================//
    //====================================================================================================================================//
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
    
    
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //========================================================================================================================================================//
    //==============================//==============================//     π+ Corrections     //==============================//==============================//
    //========================================================================================================================================================//
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
    if(corPip != 0 && ivec == 1){
        if(sec == 1){
            dp = ((-5.2e-07)*phi*phi + (-1.383e-05)*phi + (4.7179e-04))*pp*pp + ((8.33e-06)*phi*phi + (3.8849e-04)*phi + (-6.81319e-03))*pp + ((-1.645e-05)*phi*phi + (-5.0057e-04)*phi + (1.9902e-02));
        }
        if(sec == 2){
            dp = ((-1.88e-06)*phi*phi + (3.303e-05)*phi + (1.1331e-03))*pp*pp + ((1.569e-05)*phi*phi + (-3.974e-05)*phi + (-1.25869e-02))*pp + ((-2.903e-05)*phi*phi + (-1.0638e-04)*phi + (2.61529e-02));
        }
        if(sec == 3){
            dp = ((2.4e-07)*phi*phi + (-1.04e-05)*phi + (7.0864e-04))*pp*pp + ((8.0e-06)*phi*phi + (-5.156e-05)*phi + (-8.12169e-03))*pp  + ((-2.42e-05)*phi*phi + (8.928e-05)*phi + (2.13223e-02));
        }
        if(sec == 4){
            dp = ((-4.0e-08)*phi*phi + (-3.59e-05)*phi + (1.32146e-03))*pp*pp + ((1.023e-05)*phi*phi + (2.2199e-04)*phi + (-1.33043e-02))*pp + ((-2.801e-05)*phi*phi + (-1.576e-04)*phi + (3.27995e-02));
        }
        if(sec == 5){
            dp = ((2.7e-06)*phi*phi + (5.03e-06)*phi + (1.59668e-03))*pp*pp + ((-1.28e-05)*phi*phi + (-1.99e-06)*phi + (-1.71578e-02))*pp + ((2.091e-05)*phi*phi + (-4.14e-05)*phi + (3.25434e-02));
        }
        if(sec == 6){
            dp = ((2.13e-06)*phi*phi + (-7.49e-05)*phi + (1.75565e-03))*pp*pp + ((-7.37e-06)*phi*phi + (5.8222e-04)*phi + (-1.27969e-02))*pp + ((4.9e-07)*phi*phi + (-7.2253e-04)*phi + (3.11499e-02));
        }

        if(corPip == 2 || corPip == 3){
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = Corrected (Uncorrected Pion - With Elastic)][Sector 1] is:
                dp = ((-5.4904e-07)*phi*phi + (-1.4436e-05)*phi + (3.1534e-04))*pp*pp + ((3.8231e-06)*phi*phi + (3.6582e-04)*phi + (-0.0046759))*pp + ((-5.4913e-06)*phi*phi + (-4.0157e-04)*phi + (0.010767));

                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = Corrected (With (New) Pion - With Elastic)][Sector 1] is:
                dp = dp + ((6.1103e-07)*phi*phi + (5.5291e-06)*phi + (-1.9120e-04))*pp*pp + ((-3.2300e-06)*phi*phi + (1.5377e-05)*phi + (7.5279e-04))*pp + ((2.1434e-06)*phi*phi + (-6.9572e-06)*phi + (-7.9333e-05));
                dp = dp + ((-1.3049e-06)*phi*phi + (1.1295e-05)*phi + (4.5797e-04))*pp*pp + ((9.3122e-06)*phi*phi + (-5.1074e-05)*phi + (-0.0030757))*pp + ((-1.3102e-05)*phi*phi + (2.2153e-05)*phi + (0.0040938));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = Corrected (Uncorrected Pion - With Elastic)][Sector 2] is:
                dp = ((-1.0087e-06)*phi*phi + (2.1319e-05)*phi + (7.8641e-04))*pp*pp + ((6.7485e-06)*phi*phi + (7.3716e-05)*phi + (-0.0094591))*pp + ((-1.1820e-05)*phi*phi + (-3.8103e-04)*phi + (0.018936));

                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = Corrected (With (New) Pion - With Elastic)][Sector 2] is:
                dp = dp + ((8.8155e-07)*phi*phi + (-2.8257e-06)*phi + (-2.6729e-04))*pp*pp + ((-5.4499e-06)*phi*phi + (3.8397e-05)*phi + (0.0015914))*pp + ((6.8926e-06)*phi*phi + (-5.9386e-05)*phi + (-0.0021749));
                dp = dp + ((-2.0147e-07)*phi*phi + (1.1061e-05)*phi + (3.8827e-04))*pp*pp + ((4.9294e-07)*phi*phi + (-6.0257e-05)*phi + (-0.0022087))*pp + ((9.8548e-07)*phi*phi + (5.9047e-05)*phi + (0.0022905));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = Corrected (Uncorrected Pion - With Elastic)][Sector 3] is:
                dp = ((8.6722e-08)*phi*phi + (-1.7975e-05)*phi + (4.8118e-05))*pp*pp + ((2.6273e-06)*phi*phi + (3.1453e-05)*phi + (-0.0015943))*pp + ((-6.4463e-06)*phi*phi + (-5.8990e-05)*phi + (0.0041703));

                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = Corrected (With (New) Pion - With Elastic)][Sector 3] is:
                dp = dp + ((9.6317e-07)*phi*phi + (-1.7659e-06)*phi + (-8.8318e-05))*pp*pp + ((-5.1346e-06)*phi*phi + (8.3318e-06)*phi + (3.7723e-04))*pp + ((3.9548e-06)*phi*phi + (-6.9614e-05)*phi + (2.1393e-04));
                dp = dp + ((5.6438e-07)*phi*phi + (8.1678e-06)*phi + (-9.4406e-05))*pp*pp + ((-3.9074e-06)*phi*phi + (-6.5174e-05)*phi + (5.4218e-04))*pp + ((6.3198e-06)*phi*phi + (1.0611e-04)*phi + (-4.5749e-04));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = Corrected (Uncorrected Pion - With Elastic)][Sector 4] is:
                dp = ((4.3406e-07)*phi*phi + (-4.9036e-06)*phi + (2.3064e-04))*pp*pp + ((1.3624e-06)*phi*phi + (3.2907e-05)*phi + (-0.0034872))*pp + ((-5.1017e-06)*phi*phi + (2.4593e-05)*phi + (0.0092479));

                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = Corrected (With (New) Pion - With Elastic)][Sector 4] is:
                dp = dp + ((6.0218e-07)*phi*phi + (-1.4383e-05)*phi + (-3.1999e-05))*pp*pp + ((-1.1243e-06)*phi*phi + (9.3884e-05)*phi + (-4.1985e-04))*pp + ((-1.8808e-06)*phi*phi + (-1.2222e-04)*phi + (0.0014037));
                dp = dp + ((-2.5490e-07)*phi*phi + (-8.5120e-07)*phi + (7.9109e-05))*pp*pp + ((2.5879e-06)*phi*phi + (8.6108e-06)*phi + (-5.1533e-04))*pp + ((-4.4521e-06)*phi*phi + (-1.7012e-05)*phi + (7.4848e-04));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = Corrected (Uncorrected Pion - With Elastic)][Sector 5] is:
                dp = ((2.4292e-07)*phi*phi + (8.8741e-06)*phi + (2.9482e-04))*pp*pp + ((3.7229e-06)*phi*phi + (7.3215e-06)*phi + (-0.0050685))*pp + ((-1.1974e-05)*phi*phi + (-1.3043e-04)*phi + (0.0078836));

                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = Corrected (With (New) Pion - With Elastic)][Sector 5] is:
                dp = dp + ((1.0867e-06)*phi*phi + (-7.7630e-07)*phi + (-4.4930e-05))*pp*pp + ((-5.6564e-06)*phi*phi + (-1.3417e-05)*phi + (2.5224e-04))*pp + ((6.8460e-06)*phi*phi + (9.0495e-05)*phi + (-4.6587e-04));
                dp = dp + ((8.5720e-07)*phi*phi + (-6.7464e-06)*phi + (-4.0944e-05))*pp*pp + ((-4.7370e-06)*phi*phi + (5.8808e-05)*phi + (1.9047e-04))*pp + ((5.7404e-06)*phi*phi + (-1.1105e-04)*phi + (-1.9392e-04));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = Corrected (Uncorrected Pion - With Elastic)][Sector 6] is:
                dp = ((2.1191e-06)*phi*phi + (-3.3710e-05)*phi + (2.5741e-04))*pp*pp + ((-1.2915e-05)*phi*phi + (2.3753e-04)*phi + (-2.6882e-04))*pp + ((2.2676e-05)*phi*phi + (-2.3115e-04)*phi + (-0.001283));

                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = Corrected (With (New) Pion - With Elastic)][Sector 6] is:
                dp = dp + ((6.0270e-07)*phi*phi + (-6.8200e-06)*phi + (1.3103e-04))*pp*pp + ((-1.8745e-06)*phi*phi + (3.8646e-05)*phi + (-8.8056e-04))*pp + ((2.0885e-06)*phi*phi + (-3.4932e-05)*phi + (4.5895e-04));
                dp = dp + ((4.7349e-08)*phi*phi + (-5.7528e-06)*phi + (-3.4097e-06))*pp*pp + ((1.7731e-06)*phi*phi + (3.5865e-05)*phi + (-5.7881e-04))*pp + ((-9.7008e-06)*phi*phi + (-4.1836e-05)*phi + (0.0035403));
            }
        }

        if(corPip == 4 || corPip == 5){ // Corresponds to Correction = mmRP2_PipMMP2 or Correction = mmRP2_PipMMsP2
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 1] is:
                dp =       ((2.3162e-07)*phi*phi +  (1.0037e-04)*phi + (6.3605e-04))*pp*pp +  ((2.5189e-06)*phi*phi + (-6.8325e-04)*phi + (-0.0073536))*pp + ((-4.8953e-06)*phi*phi +  (3.7776e-04)*phi + (0.017481));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 2] is:
                dp =       ((2.6856e-06)*phi*phi +  (7.3145e-05)*phi +  (0.0011107))*pp*pp + ((-1.7339e-05)*phi*phi + (-4.6609e-04)*phi +   (-0.01069))*pp +  ((1.9965e-05)*phi*phi +  (2.0460e-06)*phi + (0.017721));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 3] is:
                dp =       ((1.4348e-07)*phi*phi + (-6.0459e-05)*phi +  (0.0010993))*pp*pp + ((-2.9584e-07)*phi*phi +  (4.3780e-04)*phi +  (-0.010494))*pp +  ((4.7522e-06)*phi*phi + (-3.0397e-04)*phi + (0.011763));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 4] is:
                dp =       ((7.6182e-07)*phi*phi + (-2.4537e-05)*phi + (7.4374e-04))*pp*pp + ((-3.5117e-06)*phi*phi +  (1.6932e-04)*phi + (-0.0072707))*pp +  ((6.3642e-06)*phi*phi + (-1.1886e-04)*phi + (0.014928));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 5] is:
                dp =       ((3.4726e-07)*phi*phi + (-2.5325e-06)*phi +  (0.0012672))*pp*pp + ((-2.2847e-08)*phi*phi +  (2.9380e-05)*phi +  (-0.010917))*pp +  ((3.3013e-06)*phi*phi + (-1.0943e-04)*phi + (0.014334));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 6] is:
                dp =       ((2.7008e-08)*phi*phi +  (7.9373e-06)*phi +  (0.0011934))*pp*pp + ((-6.2218e-08)*phi*phi + (-8.2899e-05)*phi + (-0.0097092))*pp +  ((1.1058e-05)*phi*phi + (-1.1152e-05)*phi + (0.0097068));
            }

            // Refinements made to this correction (kept the same name)
            // Refinements were made with the file: Single_Pion_Channel_epipX_Inbending_With_Dp_Spring_2019_Pass_2_rec_clas_V4_File_All.root
                // The refinements were created on 10/5/2023 (for V5)
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2_PipMMP2 (Pass 2 Refined Electron Correction - With Pion)][Sector 1] is:
                dp = dp +  ((8.4176e-07)*phi*phi +  (1.2005e-05)*phi + (-1.6620e-04))*pp*pp + ((-5.4513e-06)*phi*phi + (-9.3949e-05)*phi +   (0.0012257))*pp +  ((8.6315e-06)*phi*phi +  (1.1832e-04)*phi + (-0.0018008));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2_PipMMP2 (Pass 2 Refined Electron Correction - With Pion)][Sector 2] is:
                dp = dp +  ((2.8775e-07)*phi*phi +  (3.6807e-06)*phi +  (2.1783e-05))*pp*pp + ((-1.3163e-06)*phi*phi + (-4.5873e-05)*phi + (-4.1510e-04))*pp +  ((1.6431e-06)*phi*phi +  (9.8938e-05)*phi +  (0.0012463));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2_PipMMP2 (Pass 2 Refined Electron Correction - With Pion)][Sector 3] is:
                dp = dp +  ((5.3417e-08)*phi*phi + (-6.9131e-06)*phi +  (4.6364e-05))*pp*pp +  ((1.6226e-07)*phi*phi +  (5.9662e-05)*phi + (-3.8155e-04))*pp +  ((4.8169e-07)*phi*phi + (-8.2344e-05)*phi +  (2.5891e-04));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2_PipMMP2 (Pass 2 Refined Electron Correction - With Pion)][Sector 4] is:
                dp = dp + ((-2.1283e-07)*phi*phi +  (6.3134e-06)*phi +  (4.8988e-06))*pp*pp +  ((2.4374e-06)*phi*phi + (-4.4217e-05)*phi + (-1.6725e-04))*pp + ((-4.4455e-06)*phi*phi +  (6.8315e-05)*phi +  (3.5471e-04));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2_PipMMP2 (Pass 2 Refined Electron Correction - With Pion)][Sector 5] is:
                dp = dp +  ((6.0902e-07)*phi*phi +  (1.1325e-06)*phi + (-1.0441e-04))*pp*pp + ((-3.7002e-06)*phi*phi + (-8.4353e-06)*phi +  (7.3170e-04))*pp +  ((6.0250e-06)*phi*phi + (-1.6914e-06)*phi + (-0.0013206));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2_PipMMP2 (Pass 2 Refined Electron Correction - With Pion)][Sector 6] is:
                dp = dp +  ((5.5947e-07)*phi*phi + (-4.3539e-06)*phi + (-1.0766e-04))*pp*pp + ((-4.3709e-06)*phi*phi +  (2.9333e-05)*phi +  (9.7093e-04))*pp +  ((9.2126e-06)*phi*phi + (-5.9750e-05)*phi + (-0.0019547));
            }
            
            if(corPip == 5){ // Corresponds to Correction = mmRP2_PipMMsP2
                // Correction is split based on whether the momentum is greater than 4 GeV or less than 4 GeV
                if(pp >= 4){
                    if(sec == 1){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2_PipMMP2 (Pass 2 Refined Electron Correction - With Pion)][Sector 1] is:
                        dp = dp + ((-7.2027e-06)*phi*phi + (-9.6557e-05)*phi + (-6.8172e-04))*pp*pp + ((8.6596e-05)*phi*phi + (9.5750e-04)*phi + (0.0034343))*pp + ((-2.5537e-04)*phi*phi + (-0.0022122)*phi + (0.0048584));
                    }
                    if(sec == 2){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2_PipMMP2 (Pass 2 Refined Electron Correction - With Pion)][Sector 2] is:
                        dp = dp + ((-1.1001e-05)*phi*phi + (-1.2434e-04)*phi + (-0.0023145))*pp*pp + ((1.2473e-04)*phi*phi + (0.0012392)*phi + (0.0224))*pp + ((-3.5197e-04)*phi*phi + (-0.0028099)*phi + (-0.048264));
                    }
                    if(sec == 3){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2_PipMMP2 (Pass 2 Refined Electron Correction - With Pion)][Sector 3] is:
                        dp = dp + ((-2.1964e-06)*phi*phi + (9.1340e-07)*phi + (-0.002515))*pp*pp + ((2.8086e-05)*phi*phi + (6.5217e-05)*phi + (0.023951))*pp + ((-8.9256e-05)*phi*phi + (-4.2422e-04)*phi + (-0.050746));
                    }
                    if(sec == 4){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2_PipMMP2 (Pass 2 Refined Electron Correction - With Pion)][Sector 4] is:
                        dp = dp + ((-3.7147e-06)*phi*phi + (7.7026e-05)*phi + (-0.0018494))*pp*pp + ((4.7613e-05)*phi*phi + (-8.8878e-04)*phi + (0.01796))*pp + ((-1.4740e-04)*phi*phi + (0.0024937)*phi + (-0.039466));
                    }
                    if(sec == 5){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2_PipMMP2 (Pass 2 Refined Electron Correction - With Pion)][Sector 5] is:
                        dp = dp +  ((5.4313e-06)*phi*phi + (-3.1710e-05)*phi + (-0.0036724))*pp*pp + ((-5.9298e-05)*phi*phi + (4.1536e-04)*phi + (0.037361))*pp + ((1.5828e-04)*phi*phi + (-0.0013508)*phi + (-0.089146));
                    }
                    if(sec == 6){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2_PipMMP2 (Pass 2 Refined Electron Correction - With Pion)][Sector 6] is:
                        dp = dp + ((2.4524e-07)*phi*phi + (-1.1842e-04)*phi + (-0.0039563))*pp*pp + ((-1.0923e-06)*phi*phi + (0.001264)*phi + (0.040802))*pp + ((-1.3884e-06)*phi*phi + (-0.0032696)*phi + (-0.09893));
                    }
                }
            }
        }
        
        
        // Fall 2018 - Pass 2 Corrections
        if(corPip == 6){ // Corresponds to Correction = mmfaP2_ELPipMMfaP2
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMM0][Sector 1] is:
                dp = ((1.0111e-06)*phi*phi + (5.5576e-05)*phi + (-2.0734e-04))*pp*pp + ((-4.7499e-06)*phi*phi + (-6.3800e-04)*phi + (0.0017997))*pp + ((-3.6325e-06)*phi*phi + (1.0091e-04)*phi + (-4.1379e-04));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMM0][Sector 2] is:
                dp = ((3.2353e-06)*phi*phi + (3.2231e-05)*phi + (-5.2636e-04))*pp*pp + ((-2.1611e-05)*phi*phi + (-3.6647e-04)*phi + (0.0046012))*pp + ((1.9479e-05)*phi*phi + (4.8691e-05)*phi + (-0.0077236));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMM0][Sector 3] is:
                dp = ((-5.0785e-08)*phi*phi + (-1.2543e-05)*phi + (-6.5541e-05))*pp*pp + ((-2.9050e-06)*phi*phi + (1.6694e-04)*phi + (-1.6092e-06))*pp + ((8.7479e-06)*phi*phi + (-1.4064e-04)*phi + (-0.0019552));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMM0][Sector 4] is:
                dp = ((6.8155e-07)*phi*phi + (4.1069e-06)*phi + (-5.7928e-04))*pp*pp + ((-7.9321e-06)*phi*phi + (-1.1182e-05)*phi + (0.0057558))*pp + ((1.6317e-05)*phi*phi + (-2.3502e-05)*phi + (-0.015802));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMM0][Sector 5] is:
                dp = ((-9.8062e-07)*phi*phi + (1.8881e-05)*phi + (-4.3191e-04))*pp*pp + ((5.8950e-06)*phi*phi + (-1.8007e-04)*phi + (0.0054105))*pp + ((-1.6796e-05)*phi*phi + (-8.0562e-05)*phi + (-0.013527));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMM0][Sector 6] is:
                dp = ((4.8744e-07)*phi*phi + (8.0932e-05)*phi + (-8.0001e-04))*pp*pp + ((-3.6221e-06)*phi*phi + (-5.9260e-04)*phi + (0.0049435))*pp + ((3.4766e-06)*phi*phi + (3.9113e-04)*phi + (-0.013482));
            }
            
            // Refinement made from Extra_Version_Name = "Forward_Fall2018_P2_Test_V5"
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 1] is:
                dp = dp + ((9.6529e-07)*phi*phi + (-6.3808e-06)*phi + (1.6481e-04))*pp*pp + ((-7.4268e-06)*phi*phi + (1.4101e-04)*phi + (-0.0030306))*pp + ((1.0624e-05)*phi*phi + (-1.7095e-04)*phi + (0.010411));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 2] is:
                dp = dp + ((-8.0014e-07)*phi*phi + (9.0447e-06)*phi + (6.3132e-04))*pp*pp + ((8.1699e-06)*phi*phi + (6.3365e-05)*phi + (-0.0072546))*pp + ((-7.7759e-06)*phi*phi + (-3.1762e-04)*phi + (0.012731));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 3] is:
                dp = dp + ((-1.0293e-07)*phi*phi + (5.9311e-06)*phi + (3.4851e-04))*pp*pp + ((4.7281e-06)*phi*phi + (-1.1553e-04)*phi + (-0.0041831))*pp + ((-1.4566e-05)*phi*phi + (1.4323e-04)*phi + (0.01277));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 4] is:
                dp = dp + ((-3.8735e-07)*phi*phi + (-1.4431e-05)*phi + (8.2589e-04))*pp*pp + ((1.0733e-05)*phi*phi + (6.8166e-05)*phi + (-0.00904))*pp + ((-3.4539e-05)*phi*phi + (5.0404e-05)*phi + (0.026127));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 5] is:
                dp = dp + ((1.1929e-08)*phi*phi + (4.0469e-06)*phi + (0.0015612))*pp*pp + ((4.4733e-06)*phi*phi + (-3.5644e-05)*phi + (-0.015765))*pp + ((-5.6667e-06)*phi*phi + (8.1663e-05)*phi + (0.02723));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 6] is:
                dp = dp + ((1.3205e-06)*phi*phi + (-3.4827e-05)*phi + (0.0014486))*pp*pp + ((-7.2797e-06)*phi*phi + (2.2309e-04)*phi + (-0.0091902))*pp + ((8.5223e-06)*phi*phi + (-1.5744e-04)*phi + (0.018861));
            }
            
            // Refinement made from Extra_Version_Name = "Forward_Fall2018_P2_Test_V6"
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 1] is:
                dp = dp + ((-6.2255e-07)*phi*phi + (1.0214e-06)*phi + (2.5344e-04))*pp*pp + ((7.9815e-06)*phi*phi + (3.3594e-05)*phi + (-0.0027925))*pp + ((-1.8099e-05)*phi*phi + (-5.4133e-05)*phi + (0.0071398));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 2] is:
                dp = dp + ((-1.2641e-06)*phi*phi + (-1.5281e-06)*phi + (3.2149e-04))*pp*pp + ((9.2496e-06)*phi*phi + (5.0090e-05)*phi + (-0.002904))*pp + ((-1.4918e-05)*phi*phi + (-1.2946e-04)*phi + (0.0066272));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 3] is:
                dp = dp + ((2.4281e-07)*phi*phi + (-1.2261e-06)*phi + (4.4800e-05))*pp*pp + ((-1.4789e-07)*phi*phi + (-1.2145e-05)*phi + (-5.5506e-04))*pp + ((-3.7526e-07)*phi*phi + (3.6310e-05)*phi + (0.001157));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 4] is:
                dp = dp + ((2.2241e-07)*phi*phi + (-1.0564e-05)*phi + (3.5392e-04))*pp*pp + ((-5.9992e-07)*phi*phi + (5.5053e-05)*phi + (-0.0025682))*pp + ((5.4840e-06)*phi*phi + (6.0706e-06)*phi + (0.0031961));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 5] is:
                dp = dp + ((3.8356e-07)*phi*phi + (3.3064e-06)*phi + (1.2935e-04))*pp*pp + ((-4.5853e-07)*phi*phi + (-3.2460e-05)*phi + (-0.0018519))*pp + ((-2.7462e-06)*phi*phi + (7.2391e-05)*phi + (0.0060517));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 6] is:
                dp = dp + ((1.1602e-06)*phi*phi + (-1.9015e-05)*phi + (-3.6810e-05))*pp*pp + ((-6.8771e-06)*phi*phi + (1.4793e-04)*phi + (1.8771e-04))*pp + ((2.6825e-06)*phi*phi + (-2.0166e-04)*phi + (0.0037471));
            }
            
            // Refinement made from Extra_Version_Name = "Forward_Fall2018_P2_Test_V8"
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 1] is:
                dp = dp + ((-1.5386e-08)*phi*phi + (-3.0703e-06)*phi + (-6.3720e-05))*pp*pp + ((1.3492e-06)*phi*phi + (5.6471e-05)*phi + (3.5015e-04))*pp + ((-8.2798e-07)*phi*phi + (-1.0091e-04)*phi + (-0.0016961));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 2] is:
                dp = dp + ((-5.8884e-07)*phi*phi + (1.0919e-05)*phi + (9.1370e-05))*pp*pp + ((7.5700e-06)*phi*phi + (-9.0078e-05)*phi + (-0.001896))*pp + ((-1.8800e-05)*phi*phi + (1.2259e-04)*phi + (0.0034845));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 3] is:
                dp = dp + ((-7.0691e-07)*phi*phi + (-6.6656e-06)*phi + (2.5692e-04))*pp*pp + ((6.6035e-06)*phi*phi + (5.3531e-05)*phi + (-0.0030788))*pp + ((-1.0673e-05)*phi*phi + (-1.1955e-04)*phi + (0.0039758));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 4] is:
                dp = dp + ((4.2134e-07)*phi*phi + (-7.2136e-06)*phi + (-6.6800e-05))*pp*pp + ((-3.8195e-06)*phi*phi + (6.2408e-05)*phi + (2.0413e-04))*pp + ((9.2423e-06)*phi*phi + (-1.1143e-04)*phi + (-0.0027527));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 5] is:
                dp = dp + ((7.6080e-07)*phi*phi + (-4.1006e-06)*phi + (-9.5440e-05))*pp*pp + ((-7.0970e-06)*phi*phi + (6.1629e-05)*phi + (3.5178e-04))*pp + ((1.6766e-05)*phi*phi + (-1.8855e-04)*phi + (-0.0021373));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 6] is:
                dp = dp + ((-1.0246e-06)*phi*phi + (-1.3784e-05)*phi + (6.4560e-05))*pp*pp + ((9.8205e-06)*phi*phi + (1.4208e-04)*phi + (-0.001803))*pp + ((-1.3982e-05)*phi*phi + (-2.5638e-04)*phi + (0.0027303));
            }
            
            
            // Split Pion Refinement made from Extra_Version_Name = "Forward_Fall2018_P2_In_Refine_V3" (refined with full Pion Momentum + Energy Loss Corrections) - Made on 8/22/2024
            if(pp < 2.5){
                if(sec == 1){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 1] is:
                    dp = dp +  ((1.0929e-05)*phi*phi + (-3.8002e-04)*phi +   (-0.01412))*pp*pp + ((-2.8491e-05)*phi*phi +  (5.0952e-04)*phi +  (0.037728))*pp +  ((1.6927e-05)*phi*phi +  (1.8165e-04)*phi + (-0.027772));
                }
                if(sec == 2){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 2] is:
                    dp = dp +  ((9.2373e-06)*phi*phi + (-3.3151e-04)*phi +  (-0.019254))*pp*pp + ((-2.7546e-05)*phi*phi +  (5.3915e-04)*phi +  (0.052516))*pp +  ((2.5220e-05)*phi*phi +  (7.5362e-05)*phi + (-0.033504));
                }
                if(sec == 3){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 3] is:
                    dp = dp +  ((1.8595e-06)*phi*phi +  (3.6900e-04)*phi + (-0.0099622))*pp*pp +  ((8.4410e-06)*phi*phi +  (-0.0010457)*phi +  (0.027038))*pp + ((-1.2191e-05)*phi*phi +  (6.0203e-04)*phi + (-0.019176));
                }
                if(sec == 4){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 4] is:
                    dp = dp +  ((9.5779e-06)*phi*phi +  (3.5339e-04)*phi +   (-0.01054))*pp*pp + ((-1.8077e-05)*phi*phi +  (-0.0010543)*phi +  (0.028379))*pp +  ((3.1773e-06)*phi*phi +  (5.6223e-04)*phi + (-0.018865));
                }
                if(sec == 5){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 5] is:
                    dp = dp +  ((3.3685e-05)*phi*phi +  (2.8972e-04)*phi +  (-0.017862))*pp*pp + ((-8.4089e-05)*phi*phi + (-9.8038e-04)*phi +  (0.050405))*pp +  ((4.3478e-05)*phi*phi +  (6.9924e-04)*phi + (-0.033066));
                }
                if(sec == 6){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 6] is:
                    dp = dp +  ((1.7381e-05)*phi*phi +  (5.4630e-04)*phi +  (-0.019637))*pp*pp + ((-3.8681e-05)*phi*phi +  (-0.0017358)*phi +    (0.0565))*pp +  ((1.2268e-05)*phi*phi +   (0.0011412)*phi + (-0.035608));
                }
            }
            else{
                if(sec == 1){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 1] is:
                    dp = dp +  ((4.3191e-07)*phi*phi + (-9.0581e-05)*phi + (-0.0011766))*pp*pp + ((-3.6232e-06)*phi*phi +   (0.0010342)*phi +  (0.012454))*pp +  ((1.2235e-05)*phi*phi +  (-0.0025855)*phi + (-0.035323));
                }
                if(sec == 2){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 2] is:
                    dp = dp +  ((2.2654e-08)*phi*phi + (-8.8436e-05)*phi + (-0.0013542))*pp*pp +  ((3.0630e-07)*phi*phi +  (9.4319e-04)*phi +    (0.0147))*pp + ((-3.5941e-06)*phi*phi +  (-0.0022473)*phi + (-0.036874));
                }
                if(sec == 3){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 3] is:
                    dp = dp +  ((6.8265e-07)*phi*phi +  (3.0246e-05)*phi + (-0.0011116))*pp*pp + ((-4.8481e-06)*phi*phi + (-3.7082e-04)*phi +  (0.011452))*pp +  ((7.2478e-06)*phi*phi +  (9.9858e-04)*phi + (-0.027972));
                }
                if(sec == 4){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 4] is:
                    dp = dp +  ((7.7000e-07)*phi*phi +  (4.1000e-06)*phi + (-0.0010144))*pp*pp + ((-8.1960e-06)*phi*phi + (-4.7753e-05)*phi +  (0.010594))*pp +  ((2.0716e-05)*phi*phi +  (1.2151e-04)*phi + (-0.028619));
                }
                if(sec == 5){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 5] is:
                    dp = dp +  ((4.6106e-07)*phi*phi + (-3.6786e-05)*phi + (-0.0015894))*pp*pp + ((-4.4217e-06)*phi*phi +  (3.7321e-04)*phi +  (0.015917))*pp +  ((7.5188e-06)*phi*phi + (-8.0676e-04)*phi + (-0.036944));
                }
                if(sec == 6){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 6] is:
                    dp = dp + ((-8.9398e-08)*phi*phi + (-1.2347e-05)*phi + (-0.0018442))*pp*pp +  ((7.8164e-08)*phi*phi +  (1.3063e-04)*phi +   (0.01783))*pp +  ((8.2374e-06)*phi*phi + (-3.5862e-04)*phi + (-0.047011));
                }
            }
            
            
            // Pion Refinement made from Extra_Version_Name = "Forward_Fall2018_P2_In_Refine_V4" (refined with full Pion Momentum + Energy Loss Corrections) - Made on 8/23/2024
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 1] is:
                dp = dp + ((-3.7494e-07)*phi*phi + (-1.5439e-06)*phi +  (4.2760e-05))*pp*pp +  ((3.5348e-06)*phi*phi +  (4.8165e-05)*phi + (-2.3799e-04))*pp + ((-8.2116e-06)*phi*phi + (-7.1750e-05)*phi +  (1.5984e-04));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 2] is:
                dp = dp +  ((4.3694e-07)*phi*phi +  (1.1476e-05)*phi +  (1.1123e-04))*pp*pp + ((-2.4617e-06)*phi*phi + (-7.5353e-05)*phi + (-6.2511e-04))*pp + ((-1.0387e-06)*phi*phi +  (5.8447e-05)*phi +  (6.4986e-04));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 3] is:
                dp = dp +  ((1.8639e-07)*phi*phi +  (4.9444e-06)*phi + (-2.9030e-05))*pp*pp + ((-1.3752e-06)*phi*phi + (-3.3709e-05)*phi +  (3.8288e-04))*pp +  ((1.0113e-06)*phi*phi +  (5.1273e-05)*phi + (-6.7844e-04));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 4] is:
                dp = dp +  ((4.8394e-07)*phi*phi +  (3.6342e-06)*phi + (-2.0136e-04))*pp*pp + ((-3.2757e-06)*phi*phi + (-3.5397e-05)*phi +   (0.0015599))*pp +  ((3.2095e-06)*phi*phi +  (7.9013e-05)*phi + (-0.002012));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 5] is:
                dp = dp +  ((4.3113e-07)*phi*phi +  (2.6869e-06)*phi + (-2.1326e-04))*pp*pp + ((-3.1063e-06)*phi*phi + (-2.7152e-05)*phi +   (0.0017964))*pp +  ((3.1946e-06)*phi*phi +  (4.2059e-05)*phi + (-0.0031325));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 6] is:
                dp = dp +  ((4.9123e-07)*phi*phi +  (5.1828e-06)*phi + (-1.3898e-04))*pp*pp + ((-3.4108e-06)*phi*phi + (-5.0009e-05)*phi +   (0.0014879))*pp +  ((4.0320e-06)*phi*phi +  (6.5853e-05)*phi + (-0.0032227));
            }

        }
        
    }
    
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //==============================================================================================================================================================//
    //==============================//==============================//     π+ Corrections (End)     //==============================//==============================//
    //==============================================================================================================================================================//
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
    
    
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //========================================================================================================================================================//
    //==============================//==============================//     π- Corrections     //==============================//==============================//
    //========================================================================================================================================================//
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
    if(corPim != 0 && ivec == 2){
        if(sec == 1){
            dp = ((-4.0192658422317425e-06)*phi*phi - (2.660222128967742e-05)*phi + 0.004774434682983547)*pp*pp;
            dp = dp + ((1.9549520962477972e-05)*phi*phi - 0.0002456062756770577*phi - 0.03787692408323466)*pp; 
            dp = dp + (-2.128953094937459e-05)*phi*phi + 0.0002461708852239913*phi + 0.08060704449822174 - 0.01;
        }
        if(sec == 2){
            dp = ((1.193010521758372e-05)*phi*phi - (5.996221756031922e-05)*phi + 0.0009093437955814359)*pp*pp;
            dp = dp + ((-4.89113824430594e-05)*phi*phi + 0.00021676479488147118*phi - 0.01861892053916726)*pp;  
            dp = dp + (4.446394152208071e-05)*phi*phi - (3.6592784167335244e-05)*phi + 0.05498710249944096 - 0.01;
        }
        if(sec == 3){
            dp = ((-1.6596664895992133e-07)*phi*phi + (6.317189710683516e-05)*phi + 0.0016364212312654086)*pp*pp;
            dp = dp + ((-2.898409777520318e-07)*phi*phi - 0.00014531513577533802*phi - 0.025456145839203827)*pp;  
            dp = dp + (2.6432552410603506e-06)*phi*phi + 0.00018447151306275443*phi + 0.06442602664627255 - 0.01;
        }
        if(sec == 4){
            dp = ((2.4035259647558634e-07)*phi*phi - (8.649647351491232e-06)*phi + 0.004558993439848128)*pp*pp;
            dp = dp + ((-5.981498144060984e-06)*phi*phi + 0.00010582131454222416*phi - 0.033572004651981686)*pp;  
            dp = dp + (8.70140266889548e-06)*phi*phi - 0.00020137414379966883*phi + 0.07258774523336173 - 0.01;   
        }
        if(sec == 5){
            dp = ((2.5817024702834863e-06)*phi*phi + 0.00010132810066914441*phi + 0.003397314538804711)*pp*pp;
            dp = dp + ((-1.5116941263931812e-05)*phi*phi - 0.00040679799541839254*phi - 0.028144285760769876)*pp;  
            dp = dp + (1.4701931057951464e-05)*phi*phi + 0.0002426350390593454*phi + 0.06781682510174941 - 0.01;
        }
        if(sec == 6){
            dp = ((-8.196823669099362e-07)*phi*phi - (5.280412421933636e-05)*phi + 0.0018457238328451137)*pp*pp;
            dp = dp + ((5.2675062282094536e-06)*phi*phi + 0.0001515803461044587*phi - 0.02294371578470564)*pp;  
            dp = dp + (-9.459454671739747e-06)*phi*phi - 0.0002389523716779765*phi + 0.06428970810739926 - 0.01;
        }
    }
    
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //==============================================================================================================================================================//
    //==============================//==============================//     π- Corrections (End)     //==============================//==============================//
    //==============================================================================================================================================================//
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
    
    
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //================================================================================================================================================================//
    //==============================//==============================//     All Proton Corrections     //==============================//==============================//
    //================================================================================================================================================================//
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    if(corPro != 0 && ivec == 3){

        if(corPro == 1){ // Quadratic Momentum - No Phi Dependence

            if(sec == 1){
                dp = (5.415e-04)*pp*pp + (-1.0262e-02)*pp + (7.78075e-03);
                // From GitHub_F_Pro for GitHub_F2_Pro:
                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 1][All Pro Phi Bins] is:
                dp = dp + ((1.2129e-04)*pp*pp + (1.5373e-04)*pp + (-2.7084e-04));
            }

            if(sec == 2){
                dp = (-9.5439e-04)*pp*pp + (-2.86273e-03)*pp + (3.38149e-03);
                // From GitHub_F_Pro for GitHub_F2_Pro:
                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 2][All Pro Phi Bins] is:
                dp = dp + ((-1.6890e-03)*pp*pp + (4.3744e-03)*pp + (-2.1218e-03));
            }

            if(sec == 3){
                dp = (-5.5541e-04)*pp*pp + (-7.69739e-03)*pp + (5.7692e-03);
                // From GitHub_F_Pro for GitHub_F2_Pro:
                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 3][All Pro Phi Bins] is:
                dp = dp + ((7.6422e-04)*pp*pp + (-1.5425e-03)*pp + (5.4255e-04));
            }

            if(sec == 4){
                dp = (-1.944e-04)*pp*pp + (-5.77104e-03)*pp + (3.42399e-03);
                // From GitHub_F_Pro for GitHub_F2_Pro:
                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 4][All Pro Phi Bins] is:
                dp = dp + ((1.1174e-03)*pp*pp + (-3.2747e-03)*pp + (2.3687e-03));
            }

            if(sec == 5){
                dp = (1.54009e-03)*pp*pp + (-1.69437e-02)*pp + (1.04656e-02);
                // From GitHub_F_Pro for GitHub_F2_Pro:
                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 5][All Pro Phi Bins] is:
                dp = dp + ((-2.1067e-04)*pp*pp + (1.2266e-03)*pp + (-1.0553e-03));
            }

            if(sec == 6){
                dp = (2.38182e-03)*pp*pp + (-2.07301e-02)*pp + (1.72325e-02);
                // From GitHub_F_Pro for GitHub_F2_Pro:
                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 6][All Pro Phi Bins] is:
                dp = dp + ((-3.6002e-04)*pp*pp + (8.9582e-04)*pp + (-1.0093e-03));
            }
        }


        if(corPro == 2){ // Quadratic Momentum - No Phi Dependence - With Elastic
            if(sec == 1){
                // Using consistent momentum bins of 0.25 GeV per slice:
                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = Corrected - New][Sector 1][regall] is:
                dp = ((7.0897e-03)*pp*pp + (-0.03199)*pp + (0.02237));

                // Refined with a limited π0 Channel Contributions (up to Pro = 0.95 GeV - The double pion channel's range is from 0.45 to 3.1 GeV)
                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF_ProMMpro_EF][Sector 1][regall] is:
                dp = dp + ((-0.0111)*pp*pp + (0.04398)*pp + (-0.0309));
            }
            if(sec == 2){
                // Using consistent momentum bins of 0.25 GeV per slice:
                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = Corrected - New][Sector 2][regall] is:
                dp = ((5.3849e-03)*pp*pp + (-0.02474)*pp + (0.01933));

                // Refined with a limited π0 Channel Contributions (up to Pro = 0.95 GeV - The double pion channel's range is from 0.45 to 3.1 GeV)
                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF_ProMMpro_EF][Sector 2][regall] is:
                dp = dp + ((-8.3180e-03)*pp*pp + (0.03359)*pp + (-0.0251));
            }
            if(sec == 3){
                // Using consistent momentum bins of 0.25 GeV per slice:
                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = Corrected - New][Sector 3][regall] is:
                dp = ((0.01095)*pp*pp + (-0.04196)*pp + (0.02795));

                // Refined with a limited π0 Channel Contributions (up to Pro = 0.95 GeV - The double pion channel's range is from 0.45 to 3.1 GeV)
                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF_ProMMpro_EF][Sector 3][regall] is:
                dp = dp + ((-0.01892)*pp*pp + (0.06574)*pp + (-0.04358));
            }
            if(sec == 4){
                // Using consistent momentum bins of 0.25 GeV per slice:
                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = Corrected - New][Sector 4][regall] is:
                dp = ((0.01038)*pp*pp + (-0.04012)*pp + (0.02781));

                // Refined with a limited π0 Channel Contributions (up to Pro = 0.95 GeV - The double pion channel's range is from 0.45 to 3.1 GeV)
                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF_ProMMpro_EF][Sector 4][regall] is:
                dp = dp + ((-0.0147)*pp*pp + (0.05475)*pp + (-0.03912));
            }
            if(sec == 5){
                // Using consistent momentum bins of 0.25 GeV per slice:
                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = Corrected - New][Sector 5][regall] is:
                dp = ((9.0227e-03)*pp*pp + (-0.04131)*pp + (0.02748));

                // Refined with a limited π0 Channel Contributions (up to Pro = 0.95 GeV - The double pion channel's range is from 0.45 to 3.1 GeV)
                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF_ProMMpro_EF][Sector 5][regall] is:
                dp = dp + ((-0.01526)*pp*pp + (0.05599)*pp + (-0.03795));
            }
            if(sec == 6){
                // Using consistent momentum bins of 0.25 GeV per slice:
                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = Corrected - New][Sector 6][regall] is:
                dp = ((8.8531e-03)*pp*pp + (-0.03881)*pp + (0.0284));

                // Refined with a limited π0 Channel Contributions (up to Pro = 0.95 GeV - The double pion channel's range is from 0.45 to 3.1 GeV)
                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF_ProMMpro_EF][Sector 6][regall] is:
                dp = dp + ((-0.01037)*pp*pp + (0.0386)*pp + (-0.0256));
            }
        }


        if(corPro == 3){ // (Double) Quadratic Momentum - No Phi Dependence - With Elastic
            if(sec == 1){
                dp = ((1 + TMath::Sign(1, -(pp - 1.4)))/2)*((-0.0959)*pp*pp + (0.18948)*pp + (-0.08328)) + ((1 + TMath::Sign(1, (pp - 1.4)))/2)*((0.01991)*(pp - 1.4)*(pp - 1.4) + (-0.01963)*(pp - 1.4) + ((-0.0959)*1.4*1.4 + (0.18948)*1.4 + (-0.0959)));
            }
            if(sec == 2){
                dp = ((1 + TMath::Sign(1, -(pp - 1.5)))/2)*((-0.06642)*pp*pp + (0.14583)*pp + (-0.06885)) + ((1 + TMath::Sign(1, (pp - 1.5)))/2)*((0.07575)*(pp - 1.5)*(pp - 1.5) + (-0.07001)*(pp - 1.5) + ((-0.06642)*1.5*1.5 + (0.14583)*1.5 + (-0.06642)));
            }
            if(sec == 3){
                dp = ((1 + TMath::Sign(1, -(pp - 1.05)))/2)*((-0.14588)*pp*pp + (0.26771)*pp + (-0.11513)) + ((1 + TMath::Sign(1, (pp - 1.05)))/2)*((0.03042)*(pp - 1.05)*(pp - 1.05) + (-0.04788)*(pp - 1.05) + ((-0.14588)*1.05*1.05 + (0.26771)*1.05 + (-0.14588)));
            }
            if(sec == 4){
                dp = ((1 + TMath::Sign(1, -(pp - 1.4)))/2)*((-0.09563)*pp*pp + (0.19039)*pp + (-0.08607)) + ((1 + TMath::Sign(1, (pp - 1.4)))/2)*((-7.7622e-03)*(pp - 1.4)*(pp - 1.4) + (7.6980e-03)*(pp - 1.4) + ((-0.09563)*1.4*1.4 + (0.19039)*1.4 + (-0.09563)));
            }
            if(sec == 5){
                dp = ((1 + TMath::Sign(1, -(pp - 1.5)))/2)*((-0.09331)*pp*pp + (0.19028)*pp + (-0.08766)) + ((1 + TMath::Sign(1, (pp - 1.5)))/2)*((5.7742e-03)*(pp - 1.5)*(pp - 1.5) + (1.2433e-03)*(pp - 1.5) + ((-0.09331)*1.5*1.5 + (0.19028)*1.5 + (-0.09331)));
            }
            if(sec == 6){
                dp = ((1 + TMath::Sign(1, -(pp - 1.15)))/2)*((-0.12326)*pp*pp + (0.22076)*pp + (-0.09082)) + ((1 + TMath::Sign(1, (pp - 1.15)))/2)*((2.7284e-03)*(pp - 1.15)*(pp - 1.15) + (-0.01129)*(pp - 1.15) + ((-0.12326)*1.15*1.15 + (0.22076)*1.15 + (-0.12326)));
            }
        }


        if(corPro == 4 || corPro == 6){ // Linear + Quadratic Momentum - No Phi Dependence - With Elastic (Used modified slices - i.e., each momentum bin was not identically sized to increase precision where statistics allowed)
            if(sec == 1){
                // Created for V14 (As of 12-20-2022)
                dp = ((1 + TMath::Sign(1, (pp - 1.4)))/2)*((4.4034e-03)*pp + (-0.01703)) + ((1 + TMath::Sign(1, -(pp - 1.4)))/2)*((-0.10898)*(pp - 1.4)*(pp - 1.4) + (-0.09574)*(pp - 1.4) + ((4.4034e-03)*1.4 + (-0.01703)));
            }
            if(sec == 2){
                // Created for V14 (As of 12-20-2022)
                dp = ((1 + TMath::Sign(1, (pp - 1.5)))/2)*((0.01318)*pp + (-0.03403)) + ((1 + TMath::Sign(1, -(pp - 1.5)))/2)*((-0.09829)*(pp - 1.5)*(pp - 1.5) + (-0.0986)*(pp - 1.5) + ((0.01318)*1.5 + (-0.03403)));
            }
            if(sec == 3){
                // Created for V14 (As of 12-20-2022)
                dp = ((1 + TMath::Sign(1, (pp - 1.05)))/2)*((-4.7052e-03)*pp + (1.2410e-03)) + ((1 + TMath::Sign(1, -(pp - 1.05)))/2)*((-0.22721)*(pp - 1.05)*(pp - 1.05) + (-0.09702)*(pp - 1.05) + ((-4.7052e-03)*1.05 + (1.2410e-03)));
            }
            if(sec == 4){
                // Created for V14 (As of 12-20-2022)
                dp = ((1 + TMath::Sign(1, (pp - 1.4)))/2)*((-1.0900e-03)*pp + (-4.0573e-03)) + ((1 + TMath::Sign(1, -(pp - 1.4)))/2)*((-0.09236)*(pp - 1.4)*(pp - 1.4) + (-0.073)*(pp - 1.4) + ((-1.0900e-03)*1.4 + (-4.0573e-03)));
            }
            if(sec == 5){
                // Created for V14 (As of 12-20-2022)
                dp = ((1 + TMath::Sign(1, (pp - 1.5)))/2)*((7.3965e-03)*pp + (-0.02428)) + ((1 + TMath::Sign(1, -(pp - 1.5)))/2)*((-0.09539)*(pp - 1.5)*(pp - 1.5) + (-0.09263)*(pp - 1.5) + ((7.3965e-03)*1.5 + (-0.02428)));
            }
            if(sec == 6){
                // Created for V14 (As of 12-20-2022)
                dp = ((1 + TMath::Sign(1, (pp - 1.15)))/2)*((-7.6214e-03)*pp + (8.1014e-03)) + ((1 + TMath::Sign(1, -(pp - 1.15)))/2)*((-0.12718)*(pp - 1.15)*(pp - 1.15) + (-0.06626)*(pp - 1.15) + ((-7.6214e-03)*1.15 + (8.1014e-03)));
            }
        }


        if(corPro == 5){ // Quadratic Momentum - Limited π0 Channel Contributions (up to Pro = 0.95 GeV - The double pion channel's range is from 0.45 to 3.1 GeV)
            if(sec == 1){                        
                // No Pi0 Channel
                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF][Sector 1][regall] is:
                dp = ((-0.016)*pp*pp + (0.04367)*pp + (-0.02515));

                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF_ProMMpro_REF][Sector 1][regall] is:
                dp = dp + ((5.1479e-03)*pp*pp + (-0.01511)*pp + (7.8694e-03));

                // Refined for V12 (on 12-17-2022 from V10)
                dp = dp + ((1 + TMath::Sign(1, (pp - 1.275)))/2)*((8.5400e-03)*pp + (-0.01927)) + ((1 + TMath::Sign(1, -(pp - 1.275)))/2)*((-0.09972)*(pp - 1.275)*(pp - 1.275) + (-0.07965)*(pp - 1.275) + ((8.5400e-03)*1.275 + (-0.01927)));
            }
            if(sec == 2){
                // No Pi0 Channel
                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF][Sector 2][regall] is:
                dp = ((-5.4403e-03)*pp*pp + (0.0159)*pp + (-0.01021));

                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF_ProMMpro_REF][Sector 2][regall] is:
                dp = dp + ((-2.2364e-03)*pp*pp + (7.1578e-03)*pp + (-5.6010e-03));

                // Refined for V12 (on 12-17-2022 from V10)
                dp = dp + ((1 + TMath::Sign(1, (pp - 1.5)))/2)*((6.9186e-03)*pp + (-0.01614)) + ((1 + TMath::Sign(1, -(pp - 1.5)))/2)*((-0.05739)*(pp - 1.5)*(pp - 1.5) + (-0.05469)*(pp - 1.5) + ((6.9186e-03)*1.5 + (-0.01614)));
            }
            if(sec == 3){
                // No Pi0 Channel
                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF][Sector 3][regall] is:
                dp = ((-0.0145)*pp*pp + (0.04082)*pp + (-0.02562));

                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF_ProMMpro_REF][Sector 3][regall] is:
                dp = dp + ((4.1488e-03)*pp*pp + (-0.01091)*pp + (5.3172e-03));

                // Refined for V12 (on 12-17-2022 from V10)
                dp = dp + ((1 + TMath::Sign(1, (pp - 1.05)))/2)*((3.3854e-03)*pp + (-8.8397e-03)) + ((1 + TMath::Sign(1, -(pp - 1.05)))/2)*((-0.19272)*(pp - 1.05)*(pp - 1.05) + (-0.09488)*(pp - 1.05) + ((3.3854e-03)*1.05 + (-8.8397e-03)));
            }
            if(sec == 4){
                // No Pi0 Channel
                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF][Sector 4][regall] is:
                dp = ((-0.01124)*pp*pp + (0.03298)*pp + (-0.02235));

                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF_ProMMpro_REF][Sector 4][regall] is:
                dp = dp + ((-2.9293e-04)*pp*pp + (3.6047e-03)*pp + (-3.3081e-03));

                // Refined for V12 (on 12-17-2022 from V10)
                dp = dp + ((1 + TMath::Sign(1, (pp - 1.6)))/2)*((9.4470e-03)*pp + (-0.02198)) + ((1 + TMath::Sign(1, -(pp - 1.6)))/2)*((-0.03889)*(pp - 1.6)*(pp - 1.6) + (-0.04655)*(pp - 1.6) + ((9.4470e-03)*1.6 + (-0.02198)));
            }
            if(sec == 5){
                // No Pi0 Channel
                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF][Sector 5][regall] is:
                dp = ((-0.01092)*pp*pp + (0.02808)*pp + (-0.0197));

                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF_ProMMpro_REF][Sector 5][regall] is:
                dp = dp + ((1.4513e-03)*pp*pp + (-6.5134e-03)*pp + (4.6868e-03));

                // Refined for V12 (on 12-17-2022 from V10)
                dp = dp + ((1 + TMath::Sign(1, (pp - 1.3)))/2)*((8.3686e-04)*pp + (-2.4123e-03)) + ((1 + TMath::Sign(1, -(pp - 1.3)))/2)*((-0.07312)*(pp - 1.3)*(pp - 1.3) + (-0.04876)*(pp - 1.3) + ((8.3686e-04)*1.3 + (-2.4123e-03)));
            }
            if(sec == 6){
                // No Pi0 Channel
                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF][Sector 6][regall] is:
                dp = ((-8.2723e-03)*pp*pp + (0.02055)*pp + (-0.01167));

                // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF_ProMMpro_REF][Sector 6][regall] is:
                dp = dp + ((-1.6250e-03)*pp*pp + (5.6738e-03)*pp + (-3.8019e-03));

                // Refined for V12 (on 12-17-2022 from V10)
                dp = dp + ((1 + TMath::Sign(1, (pp - 1.15)))/2)*((5.3711e-03)*pp + (-0.01317)) + ((1 + TMath::Sign(1, -(pp - 1.15)))/2)*((-0.12512)*(pp - 1.15)*(pp - 1.15) + (-0.08387)*(pp - 1.15) + ((5.3711e-03)*1.15 + (-0.01317)));
            }
        }

        if(corPro == 12){
            if(sec == 1){
                dp = ((1 + TMath::Sign(1, -(pp - (1.37961))))/2)*((-0.10988)*pp*pp + (0.17061)*pp + (-0.04566)) + ((1 + TMath::Sign(1, (pp - (1.37961))))/2)*((-0.02395)*(pp - (1.37961))*(pp - (1.37961)) + (0.0188)*(pp - (1.37961)) + ((-0.10988)*(1.37961)*(1.37961) + (0.17061)*(1.37961) + (-0.04566)));
            }
            if(sec == 2){
                dp = ((1 + TMath::Sign(1, -(pp - (0.90061))))/2)*((0.2957)*pp*pp + (-0.45727)*pp + (0.18551)) + ((1 + TMath::Sign(1, (pp - (0.90061))))/2)*((0.0142)*(pp - (0.90061))*(pp - (0.90061)) + (-0.03563)*(pp - (0.90061)) + ((0.2957)*(0.90061)*(0.90061) + (-0.45727)*(0.90061) + (0.18551)));
            }
            if(sec == 3){
                dp = ((1 + TMath::Sign(1, -(pp - (0.97528))))/2)*((0.07708)*pp*pp + (-0.10793)*pp + (0.0479)) + ((1 + TMath::Sign(1, (pp - (0.97528))))/2)*((0.01151)*(pp - (0.97528))*(pp - (0.97528)) + (-0.03167)*(pp - (0.97528)) + ((0.07708)*(0.97528)*(0.97528) + (-0.10793)*(0.97528) + (0.0479)));
            }
            if(sec == 4){
                dp = ((1 + TMath::Sign(1, -(pp - (0.94952))))/2)*((0.12712)*pp*pp + (-0.18059)*pp + (0.07288)) + ((1 + TMath::Sign(1, (pp - (0.94952))))/2)*((1.4963e-03)*(pp - (0.94952))*(pp - (0.94952)) + (-0.01659)*(pp - (0.94952)) + ((0.12712)*(0.94952)*(0.94952) + (-0.18059)*(0.94952) + (0.07288)));
            }
            if(sec == 5){
                dp = ((1 + TMath::Sign(1, -(pp - (1.16982))))/2)*((-9.4111e-03)*pp*pp + (0.01929)*pp + (2.4572e-03)) + ((1 + TMath::Sign(1, (pp - (1.16982))))/2)*((0.02872)*(pp - (1.16982))*(pp - (1.16982)) + (-0.05903)*(pp - (1.16982)) + ((-9.4111e-03)*(1.16982)*(1.16982) + (0.01929)*(1.16982) + (2.4572e-03)));
            }
            if(sec == 6){
                dp = ((1 + TMath::Sign(1, -(pp - (0.92377))))/2)*((-5.6309e-03)*pp*pp + (7.1724e-03)*pp + (0.01738)) + ((1 + TMath::Sign(1, (pp - (0.92377))))/2)*((2.0807e-03)*(pp - (0.92377))*(pp - (0.92377)) + (-0.02525)*(pp - (0.92377)) + ((-5.6309e-03)*(0.92377)*(0.92377) + (7.1724e-03)*(0.92377) + (0.01738)));
            }
        }

        if(corPro == 13){
            if(sec == 1){
                dp = ((1 + TMath::Sign(1, -(pp - (1.4681))))/2)*((-0.07881)*pp*pp + (0.12097)*pp + (-0.02689)) + ((1 + TMath::Sign(1, (pp - (1.4681))))/2)*((-0.05413)*(pp - (1.4681))*(pp - (1.4681)) + (0.06397)*(pp - (1.4681)) + ((-0.07881)*(1.4681)*(1.4681) + (0.12097)*(1.4681) + (-0.02689)));
            }
            if(sec == 2){
                dp = ((1 + TMath::Sign(1, -(pp - (0.83137))))/2)*((-0.0252)*pp*pp + (1.9204e-03)*pp + (0.02614)) + ((1 + TMath::Sign(1, (pp - (0.83137))))/2)*((3.0648e-03)*(pp - (0.83137))*(pp - (0.83137)) + (-0.01249)*(pp - (0.83137)) + ((-0.0252)*(0.83137)*(0.83137) + (1.9204e-03)*(0.83137) + (0.02614)));
            }
            if(sec == 3){
                dp = ((1 + TMath::Sign(1, -(pp - (1.81971))))/2)*((-0.01604)*pp*pp + (0.02618)*pp + (1.3139e-03)) + ((1 + TMath::Sign(1, (pp - (1.81971))))/2)*((-0.0198)*(pp - (1.81971))*(pp - (1.81971)) + (0.01804)*(pp - (1.81971)) + ((-0.01604)*(1.81971)*(1.81971) + (0.02618)*(1.81971) + (1.3139e-03)));
            }
            if(sec == 4){
                dp = ((1 + TMath::Sign(1, -(pp - (1.1))))/2)*((0.10967)*pp*pp + (-0.17521)*pp + (0.07558)) + ((1 + TMath::Sign(1, (pp - (1.1))))/2)*((7.3136e-03)*(pp - (1.1))*(pp - (1.1)) + (-0.02294)*(pp - (1.1)) + ((0.10967)*(1.1)*(1.1) + (-0.17521)*(1.1) + (0.07558)));
            }
            if(sec == 5){
                dp = ((1 + TMath::Sign(1, -(pp - (1.3247))))/2)*((-4.8153e-03)*pp*pp + (8.2971e-04)*pp + (0.01374)) + ((1 + TMath::Sign(1, (pp - (1.3247))))/2)*((-2.7883e-03)*(pp - (1.3247))*(pp - (1.3247)) + (-0.01603)*(pp - (1.3247)) + ((-4.8153e-03)*(1.3247)*(1.3247) + (8.2971e-04)*(1.3247) + (0.01374)));
            }
            if(sec == 6){
                dp = ((1 + TMath::Sign(1, -(pp - (1.075))))/2)*((-0.01358)*pp*pp + (9.8430e-04)*pp + (0.02437)) + ((1 + TMath::Sign(1, (pp - (1.075))))/2)*((8.9354e-03)*(pp - (1.075))*(pp - (1.075)) + (-0.01746)*(pp - (1.075)) + ((-0.01358)*(1.075)*(1.075) + (9.8430e-04)*(1.075) + (0.02437)));
            }
        }

        if(corPro == 14){
            if(sec == 1){
                dp = ((1 + TMath::Sign(1, -(pp - (1.42692))))/2)*((-0.10673)*pp*pp + (0.17056)*pp + (-0.04586)) + ((1 + TMath::Sign(1, (pp - (1.42692))))/2)*((-0.03061)*(pp - (1.42692))*(pp - (1.42692)) + (0.02836)*(pp - (1.42692)) + ((-0.10673)*(1.42692)*(1.42692) + (0.17056)*(1.42692) + (-0.04586)));
            }
            if(sec == 2){
                dp = ((1 + TMath::Sign(1, -(pp - (0.82618))))/2)*((0.18658)*pp*pp + (-0.29765)*pp + (0.13182)) + ((1 + TMath::Sign(1, (pp - (0.82618))))/2)*((0.01199)*(pp - (0.82618))*(pp - (0.82618)) + (-0.03199)*(pp - (0.82618)) + ((0.18658)*(0.82618)*(0.82618) + (-0.29765)*(0.82618) + (0.13182)));
            }
            if(sec == 3){
                dp = ((1 + TMath::Sign(1, -(pp - (0.97431))))/2)*((0.05887)*pp*pp + (-0.0819)*pp + (0.03947)) + ((1 + TMath::Sign(1, (pp - (0.97431))))/2)*((0.0115)*(pp - (0.97431))*(pp - (0.97431)) + (-0.03073)*(pp - (0.97431)) + ((0.05887)*(0.97431)*(0.97431) + (-0.0819)*(0.97431) + (0.03947)));
            }
            if(sec == 4){
                dp = ((1 + TMath::Sign(1, -(pp - (1.12335))))/2)*((0.04921)*pp*pp + (-0.0722)*pp + (0.03733)) + ((1 + TMath::Sign(1, (pp - (1.12335))))/2)*((6.2541e-03)*(pp - (1.12335))*(pp - (1.12335)) + (-0.02645)*(pp - (1.12335)) + ((0.04921)*(1.12335)*(1.12335) + (-0.0722)*(1.12335) + (0.03733)));
            }
            if(sec == 5){
                dp = ((1 + TMath::Sign(1, -(pp - (1.174))))/2)*((0.02769)*pp*pp + (-0.0443)*pp + (0.02957)) + ((1 + TMath::Sign(1, (pp - (1.174))))/2)*((0.01511)*(pp - (1.174))*(pp - (1.174)) + (-0.04819)*(pp - (1.174)) + ((0.02769)*(1.174)*(1.174) + (-0.0443)*(1.174) + (0.02957)));
            }
            if(sec == 6){
                dp = ((1 + TMath::Sign(1, -(pp - (1.05172))))/2)*((-5.2223e-03)*pp*pp + (5.0774e-03)*pp + (0.01891)) + ((1 + TMath::Sign(1, (pp - (1.05172))))/2)*((2.1664e-04)*(pp - (1.05172))*(pp - (1.05172)) + (-0.02573)*(pp - (1.05172)) + ((-5.2223e-03)*(1.05172)*(1.05172) + (5.0774e-03)*(1.05172) + (0.01891)));
            }
        }

        if(corPro == 15){
            if(sec == 1){
                dp = ((1 + TMath::Sign(1, -(pp - (1.42692))))/2)*((-0.10673)*pp*pp + (0.17056)*pp + (-0.04586)) + ((1 + TMath::Sign(1, (pp - (1.42692))))/2)*((-0.03061)*(pp - (1.42692))*(pp - (1.42692)) + (0.02836)*(pp - (1.42692)) + ((-0.10673)*(1.42692)*(1.42692) + (0.17056)*(1.42692) + (-0.04586)));
            }
            if(sec == 2){
                dp = ((1 + TMath::Sign(1, -(pp - (0.82618))))/2)*((0.18658)*pp*pp + (-0.29765)*pp + (0.13182)) + ((1 + TMath::Sign(1, (pp - (0.82618))))/2)*((0.01199)*(pp - (0.82618))*(pp - (0.82618)) + (-0.03199)*(pp - (0.82618)) + ((0.18658)*(0.82618)*(0.82618) + (-0.29765)*(0.82618) + (0.13182)));
            }
            if(sec == 3){
                dp = ((1 + TMath::Sign(1, -(pp - (0.97431))))/2)*((0.05887)*pp*pp + (-0.0819)*pp + (0.03947)) + ((1 + TMath::Sign(1, (pp - (0.97431))))/2)*((0.0115)*(pp - (0.97431))*(pp - (0.97431)) + (-0.03073)*(pp - (0.97431)) + ((0.05887)*(0.97431)*(0.97431) + (-0.0819)*(0.97431) + (0.03947)));
            }
            if(sec == 4){
                dp = ((1 + TMath::Sign(1, -(pp - (1.12335))))/2)*((0.04921)*pp*pp + (-0.0722)*pp + (0.03733)) + ((1 + TMath::Sign(1, (pp - (1.12335))))/2)*((6.2541e-03)*(pp - (1.12335))*(pp - (1.12335)) + (-0.02645)*(pp - (1.12335)) + ((0.04921)*(1.12335)*(1.12335) + (-0.0722)*(1.12335) + (0.03733)));
            }
            if(sec == 5){
                dp = ((1 + TMath::Sign(1, -(pp - (1.26673))))/2)*((-0.07969)*pp*pp + (0.09716)*pp + (-0.01131)) + ((1 + TMath::Sign(1, (pp - (1.26673))))/2)*((2.5671e-03)*(pp - (1.26673))*(pp - (1.26673)) + (-8.4397e-03)*(pp - (1.26673)) + ((-0.07969)*(1.26673)*(1.26673) + (0.09716)*(1.26673) + (-0.01131)));
            }
            if(sec == 6){
                dp = ((1 + TMath::Sign(1, -(pp - (0.97449))))/2)*((-0.02624)*pp*pp + (-9.6652e-04)*pp + (0.03259)) + ((1 + TMath::Sign(1, (pp - (0.97449))))/2)*((7.1481e-03)*(pp - (0.97449))*(pp - (0.97449)) + (-0.0298)*(pp - (0.97449)) + ((-0.02624)*(0.97449)*(0.97449) + (-9.6652e-04)*(0.97449) + (0.03259)));
            }
        }
        
        if(corPro == 16){
            dp = 0.02;
        }
        
        if(corPro == 17){
            dp = -0.02;
        }
    }

    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //===================================================================================================================================================================//
    //==============================//==============================//     End of Proton Corrections     //==============================//==============================//
    //===================================================================================================================================================================//
    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    return dp/pp;
};

"""])

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

###################################################################################
#----------#      Last updated Outbending Corrections on: 8-15-2024    #----------#
###################################################################################
Correction_Code_Full_Out = "".join(["""

auto dppC = [&](float Px, float Py, float Pz, int sec, int ivec, int corEl, int corPip, int corPim, int corPro){
    
    // 'sec' Corresponds to the Forward Detector Sectors where the given particle is detected (6 total)
    // For particles detected in the Central Detector, set the value of 'sec' to be any number greater than 6 (this code will automatically reassign the values of this input to be consistent with the definitions used by the corrections)
    
    // ivec = 0 --> Electron Corrections
    // ivec = 1 --> Pi+ Corrections
    // ivec = 2 --> Pi- Corrections
    // ivec = 3 --> Proton Corrections

    // corEl ==> Gives the 'generation' of the electron correction
        // corEl == 0 --> No Correction
        // corEl == 1 --> Old Version of Corrections
        // corEl == 2 --> Extended Version of Corrections (Initial/test versions)
        // corEl == 3 --> Final Extended Version of Corrections (Final Refinement)
        // corEl == 4 --> New (Fall 2018) Pass 2 Correction (w/Pion Energy Loss)

    // corPip ==> Gives the 'generation' of the π+ Pion correction
        // corPip == 0 --> No Correction
        // corPip == 1 --> Old Version of Corrections
        // corPip == 2 --> Extended Version of Corrections (Initial/test versions) - Uses corEl = 2 (or 3)
        // corPip == 3 --> Final (Extended) Version of Corrections - Uses corEl = 2 (or 3)
        // corPip == 4 --> New (Fall 2018) Pass 2 Correction (w/Pion Energy Loss) - Uses corEl = 4

    // corPim ==> Gives the 'generation' of the π- Pion correction
        // corPim == 0 --> No Correction
        // corPim == 1 --> Nick's Quadratic Momentum, Quadratic Phi

    // corPro ==> Gives the 'generation' of the Proton correction
        // corPro == 0 --> No Correction
        // corPro == 1 --> Quad Momentum, NO Phi


    // Momentum Magnitude
    double pp = sqrt(Px*Px + Py*Py + Pz*Pz);

    // Initializing the correction factor
    double dp = 0;

    // Defining Phi Angle
    double Phi = (180/3.1415926)*atan2(Py, Px);

    // Central Detector Corrections
    if(sec > 6){
        if(ivec == 1){
            // For Central Detector π+ Pions
            """, str(str(str(Central_Detector_Sector_Definition).replace("pipP", "P")).replace("pip-", "pp-")).replace("pipsec", "sec"), """
            sec = tempsec; // New Definition of Central Detector Sectors
            if(sec == 7 && Phi_Shift > 200){Phi_Shift += -360;}
            double phi = Phi_Shift - (sec - 7)*60 - 30;
            // Central Detector Corrections for the π+ Pion go here (not made yet)
            return dp/pp;
        }
        else{return dp/pp;} // Central Detector Sectors/Corrections are not yet set up for particles other than the π+ Pion
    }

    // (Initial) Shift of the Phi Angle (done to realign sectors whose data is separated when plotted from ±180˚)
    if(((sec == 4 || sec == 3) && Phi < 0) || (sec > 4 && Phi < 90)){
        Phi += 360;
    }

    // Getting Local Phi Angle
    double PhiLocal = Phi - (sec - 1)*60;

    // Applying Shift Functions to Phi Angles (local shifted phi = phi)
    double phi = PhiLocal;

    // For Electron Shift
    if(ivec == 0){
        phi = PhiLocal - 30/pp;
    }

    // For π+ Pion/Proton Shift
    if(ivec == 1 || ivec == 3){
        phi = PhiLocal + (32/(pp-0.05));
    }

    // For π- Pion Shift
    if(ivec == 2){
        phi = PhiLocal - (32/(pp-0.05));
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////
    //===============//===============//     No Corrections     //===============//===============//
    ////////////////////////////////////////////////////////////////////////////////////////////////

    if(corEl == 0  && ivec == 0){ // No Electron Correction
        dp = 0;
    }
    if(corPip == 0 && ivec == 1){ // No π+ Correction
        dp = 0;
    }
    if(corPim == 0 && ivec == 2){ // No π- Correction
        dp = 0;
    }
    if(corPro == 0 && ivec == 3){ // No Proton Correction
        dp = 0;
    }

    //////////////////////////////////////////////////////////////////////////////////////////////////
    //==============//==============//     No Corrections (End)     //==============//==============//
    //////////////////////////////////////////////////////////////////////////////////////////////////
    
    
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //==================================================================================================================================//
    //=======================//=======================//     Electron Corrections     //=======================//=======================//
    //==================================================================================================================================//
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    if(ivec == 0 && corEl != 0){
        // Old Corrections (mmF)
        if(sec == 1){
            dp = ((-7.68e-06)*phi*phi + (4.636e-05)*phi + (4.7165e-04))*pp*pp + ((1.2086e-04)*phi*phi + (2.09591e-05)*phi + (-0.01582))*pp + ((-4.1002e-04)*phi*phi + (1.7298e-04)*phi + (0.10544));
            dp = dp + ((7.51e-06)*phi*phi + (6.45e-06)*phi + (-0.00152778))*pp*pp + ((-0.00011089)*phi*phi + (-0.00017683)*phi + (0.02131197))*pp + ((0.00037962)*phi*phi + (0.00060197)*phi + (-0.06886547));                    
        }
        if(sec == 2){
            dp = ((-2.69e-06)*phi*phi + (9.252e-05)*phi + (5.1693e-04))*pp*pp + ((3.016e-05)*phi*phi + (-6.0141e-04)*phi + (-0.0146))*pp + ((-6.09e-05)*phi*phi + (1.604e-03)*phi + (0.09208));
            dp = dp + ((1.24e-06)*phi*phi + (-4.735e-05)*phi + (-0.00150312))*pp*pp + ((-2.097e-05)*phi*phi + (0.00049518)*phi + (0.01920915))*pp + ((7.474e-05)*phi*phi + (-0.00132086)*phi + (-0.05686766));                    
        }
        if(sec == 3){
            dp = ((-1.045e-05)*phi*phi + (-6.491e-05)*phi + (1.1362e-03))*pp*pp + ((1.2512e-04)*phi*phi + (5.3421e-04)*phi + (-0.0174))*pp + ((-3.0891e-04)*phi*phi + (-1.5332e-03)*phi + (0.09389));
            dp = dp + ((6.94e-06)*phi*phi + (4.271e-05)*phi + (-0.00182765))*pp*pp + ((-8.322e-05)*phi*phi + (-0.00042238)*phi + (0.01994986))*pp + ((0.00021956)*phi*phi + (0.00103844)*phi + (-0.04956505));                    
        }
        if(sec == 4){
            dp = ((-7.37e-06)*phi*phi + (-8.13e-06)*phi + (9.2425e-04))*pp*pp + ((1.1312e-04)*phi*phi + (-5.24444e-05)*phi + (-0.022944))*pp + ((-3.518e-04)*phi*phi + (3.1893e-04)*phi + (0.1323));
            dp = dp + ((8.74e-06)*phi*phi + (-1.617e-05)*phi + (-0.00173764))*pp*pp + ((-0.00011774)*phi*phi + (0.00024329)*phi + (0.02310896))*pp + ((0.00036368)*phi*phi + (-0.00076238)*phi + (-0.07050779));
        }
        if(sec == 5){
            dp = ((-8.17e-06)*phi*phi + (-1.681e-05)*phi + (7.8066e-04))*pp*pp + ((1.4176e-04)*phi*phi + (4.1096e-04)*phi + (-0.026944))*pp + ((-4.4153e-04)*phi*phi + (-1.3535e-03)*phi + (0.1486));
            dp = dp + ((7.69e-06)*phi*phi + (1.774e-05)*phi + (-1.57552e-03))*pp*pp + ((-1.0778e-04)*phi*phi + (-2.6133e-04)*phi + (0.02076174))*pp + ((3.196e-04)*phi*phi + (8.8134e-04)*phi + (-0.06204126));
        }
        if(sec == 6){
            dp = ((1.63e-06)*phi*phi + (6.251e-05)*phi + (-2.2457e-04))*pp*pp + ((8.18e-06)*phi*phi + (-6.688e-04)*phi + (4.2875e-04))*pp + ((-2.172e-05)*phi*phi + (1.5467e-03)*phi + (0.05676));
            dp = dp + ((1.34e-06)*phi*phi + (-1.574e-05)*phi + (-0.00133653))*pp*pp + ((-1.991e-05)*phi*phi + (0.00024404)*phi + (0.01428837))*pp + ((5.149e-05)*phi*phi + (-0.0007992)*phi + (-0.03467815));
        }

        // Extended Corrections Test (mmExF)
        if(corEl == 2){
            if(sec == 1){
                dp =       ((2.6957e-06)*phi*phi + (1.41185e-05)*phi + (-8.54848e-04))*pp*pp + ((-4.3470e-05)*phi*phi + (3.66281e-04)*phi +  (0.01007791))*pp +  ((1.9932e-04)*phi*phi + (-8.11713e-04)*phi + (-0.008384375));
                dp = dp + ((-7.6847e-06)*phi*phi +  (4.1267e-05)*phi +  (-7.4240e-04))*pp*pp +  ((1.2218e-04)*phi*phi + (-4.9847e-04)*phi +   (0.0088033))*pp + ((-4.9434e-04)*phi*phi +     (0.001114)*phi + (-0.021955));
                dp = dp +  ((1.3641e-05)*phi*phi + (-1.5731e-05)*phi +  (-8.7395e-04))*pp*pp + ((-1.8416e-04)*phi*phi +  (9.9110e-05)*phi +    (0.010497))*pp +  ((6.2267e-04)*phi*phi +   (2.5877e-04)*phi + (-0.028027));
                dp = dp + ((-7.3331e-06)*phi*phi +  (2.9512e-06)*phi +   (1.4857e-04))*pp*pp +  ((9.4041e-05)*phi*phi +  (5.5267e-05)*phi + (-5.8894e-04))*pp + ((-3.0270e-04)*phi*phi +  (-5.5944e-04)*phi + (-0.0034499));
            }
            if(sec == 1){
                dp =      ((1.31890e-06)*phi*phi + (4.26057e-05)*phi + (-0.002322628))*pp*pp + ((-1.140900000e-05)*phi*phi + (2.218800000e-05)*phi + (0.02878927))*pp + ((2.495000000e-05)*phi*phi + (1.617000000e-06)*phi + (-0.061816275));
            }
            if(sec == 2){
                dp =      ((-5.7393e-06)*phi*phi + (-1.217322e-05)*phi + (-3.59798e-04))*pp*pp +  ((6.3547e-05)*phi*phi + (6.47806e-04)*phi + (0.00561929))*pp + ((-1.51718e-04)*phi*phi +  (-0.00195272)*phi + (-0.0100398));
                dp = dp +  ((7.0884e-06)*phi*phi +    (8.7982e-06)*phi +   (-0.0010783))*pp*pp + ((-1.0109e-04)*phi*phi + (-1.1700e-04)*phi +   (0.012013))*pp +   ((3.3792e-04)*phi*phi +   (2.8723e-04)*phi + (-0.025106));
                dp = dp + ((-1.6415e-06)*phi*phi +    (3.6995e-06)*phi +  (-4.1021e-04))*pp*pp +  ((3.7988e-05)*phi*phi + (-5.4482e-05)*phi +  (0.0045624))*pp +  ((-1.7928e-04)*phi*phi +   (1.3032e-04)*phi + (-0.01276));
            }
            if(sec == 3){
                dp =     ((-4.84189e-06)*phi*phi + (-2.772552e-05)*phi + (-5.87211e-04))*pp*pp + ((5.40286e-05)*phi*phi + (1.739683e-04)*phi + (0.01062548))*pp + ((-9.6672e-05)*phi*phi + (-3.63641e-04)*phi + (-0.01983092));
                dp = dp +  ((7.5610e-06)*phi*phi +    (4.4297e-05)*phi +    (-0.001235))*pp*pp + ((-1.0371e-04)*phi*phi +  (-5.5008e-04)*phi +   (0.015016))*pp +  ((2.9442e-04)*phi*phi +    (0.0013219)*phi + (-0.038352));
            }
            if(sec == 4){
                dp =      ((9.2070e-07)*phi*phi + (-3.1801e-05)*phi + (-9.9342e-04))*pp*pp + ((-5.6000e-06)*phi*phi + (3.37922e-04)*phi + (0.0127541))*pp + ((1.9148e-05)*phi*phi + (-0.001328248)*phi + (-0.01868997));
                dp = dp + ((9.8896e-07)*phi*phi +  (7.0400e-06)*phi +  (-0.0013222))*pp*pp + ((-1.8327e-05)*phi*phi + (-1.1266e-04)*phi +  (0.016429))*pp + ((6.1367e-05)*phi*phi +   (6.8615e-04)*phi + (-0.042902));
            }
            if(sec == 5){
                dp =    ((9.3229677e-06)*phi*phi + (3.51099e-05)*phi + (-0.0021918953))*pp*pp + ((-1.220143e-04)*phi*phi + (-3.22997e-04)*phi + (0.02648059))*pp + ((3.96753e-04)*phi*phi + (7.7590e-04)*phi + (-0.0807585));
                dp = dp + ((-1.2999e-05)*phi*phi +  (5.3299e-06)*phi +   (-4.8562e-06))*pp*pp +    ((1.7110e-04)*phi*phi +  (-1.1444e-04)*phi + (-0.0015372))*pp + ((-5.0501e-04)*phi*phi + (6.8521e-04)*phi + (0.01591));
            }
            if(sec == 6){
                dp =     ((2.503612e-06)*phi*phi + (2.68581e-05)*phi + (-0.00139564))*pp*pp + ((-2.2352e-05)*phi*phi + (-2.05667e-04)*phi + (0.0233939))*pp + ((1.02934e-04)*phi*phi +  (6.1117e-04)*phi + (-0.059224)); 
                dp = dp + ((-2.5661e-06)*phi*phi + (-4.5408e-06)*phi + (-8.7958e-04))*pp*pp +  ((4.0724e-05)*phi*phi +   (1.3044e-04)*phi + (0.0092421))*pp + ((-1.6950e-04)*phi*phi + (-8.5567e-04)*phi + (-0.013069));
            }
        }

        // Final (Refined) Extended Corrections (mmEF)
        if(corEl == 3){
            if(sec == 1){
                dp =     ((1.3189e-06)*phi*phi +  (4.26057e-05)*phi +  (-0.002322628))*pp*pp +  ((-1.1409e-05)*phi*phi +    (2.2188e-05)*phi + (0.02878927))*pp +   ((2.4950e-05)*phi*phi +   (1.6170e-06)*phi + (-0.061816275));
            }
            if(sec == 2){
                dp =    ((-2.9240e-07)*phi*phi +   (3.2448e-07)*phi +  (-0.001848308))*pp*pp +   ((4.4500e-07)*phi*phi +   (4.76324e-04)*phi + (0.02219469))*pp +   ((6.9220e-06)*phi*phi +  (-0.00153517)*phi + (-0.0479058));
            }
            if(sec == 3){
                dp =    ((2.71911e-06)*phi*phi + (1.657148e-05)*phi +  (-0.001822211))*pp*pp + ((-4.96814e-05)*phi*phi + (-3.761117e-04)*phi + (0.02564148))*pp +  ((1.97748e-04)*phi*phi +  (9.58259e-04)*phi + (-0.05818292));
            }
            if(sec == 4){
                dp =    ((1.90966e-06)*phi*phi +  (-2.4761e-05)*phi +   (-0.00231562))*pp*pp +  ((-2.3927e-05)*phi*phi +   (2.25262e-04)*phi +  (0.0291831))*pp +   ((8.0515e-05)*phi*phi + (-6.42098e-04)*phi + (-0.06159197));
            }
            if(sec == 5){
                dp = ((-3.6760323e-06)*phi*phi +  (4.04398e-05)*phi + (-0.0021967515))*pp*pp +  ((4.90857e-05)*phi*phi +  (-4.37437e-04)*phi + (0.02494339))*pp + ((-1.08257e-04)*phi*phi +   (0.00146111)*phi + (-0.0648485));
            }
            if(sec == 6){
                dp =    ((-6.2488e-08)*phi*phi +  (2.23173e-05)*phi +   (-0.00227522))*pp*pp +   ((1.8372e-05)*phi*phi +   (-7.5227e-05)*phi +   (0.032636))*pp +  ((-6.6566e-05)*phi*phi +  (-2.4450e-04)*phi + (-0.072293));
            }
        }
        
        // New (Fall 2018 Pass 2) Corrections (mmfaP2)
        if(corEl == 4){
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mm0_ELPipMM0][Sector 1] is:
                dp =  ((1.2071e-06)*phi*phi +  (4.3200e-06)*phi + (-2.9744e-04))*pp*pp + ((-2.1188e-05)*phi*phi +  (8.4530e-05)*phi + (-0.0026927))*pp +  ((1.1271e-04)*phi*phi +  (-0.0011804)*phi + (0.058173));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mm0_ELPipMM0][Sector 2] is:
                dp = ((-1.0319e-06)*phi*phi +  (1.2265e-05)*phi +  (5.6840e-05))*pp*pp +  ((1.0772e-05)*phi*phi +  (5.1295e-05)*phi + (-0.0071982))*pp + ((-1.0130e-06)*phi*phi +  (-0.0010885)*phi + (0.062324));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mm0_ELPipMM0][Sector 3] is:
                dp = ((-2.1405e-06)*phi*phi +  (2.8517e-05)*phi +  (2.3838e-04))*pp*pp +  ((2.6409e-05)*phi*phi + (-3.5734e-04)*phi +  (-0.010347))*pp + ((-7.5798e-05)*phi*phi +  (9.5756e-04)*phi + (0.073785));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mm0_ELPipMM0][Sector 4] is:
                dp =  ((7.9694e-07)*phi*phi + (-9.9183e-06)*phi + (-8.0044e-04))*pp*pp + ((-1.0736e-05)*phi*phi +  (9.3418e-05)*phi +  (0.0037634))*pp +  ((4.8380e-05)*phi*phi + (-9.0674e-05)*phi + (0.042234));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mm0_ELPipMM0][Sector 5] is:
                dp = ((-1.4177e-07)*phi*phi + (-2.0421e-06)*phi + (-8.8740e-05))*pp*pp + ((-2.1774e-07)*phi*phi +  (1.5198e-04)*phi + (-0.0076431))*pp +  ((3.1022e-05)*phi*phi +  (-0.0010169)*phi + (0.076225));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mm0_ELPipMM0][Sector 6] is:
                dp =  ((2.7768e-06)*phi*phi +  (5.7209e-05)*phi +   (-0.001268))*pp*pp + ((-5.0133e-05)*phi*phi + (-5.2902e-04)*phi +  (0.0096535))*pp +  ((2.5264e-04)*phi*phi +  (5.8752e-04)*phi + (0.029426));
            }
            
            // Refinement Made on 7/23/2024
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMM0][Sector 1] is:
                dp = dp + ((-1.4355e-06)*phi*phi + (-8.4946e-06)*phi + (-5.4799e-04))*pp*pp +  ((3.2893e-05)*phi*phi +  (1.0950e-04)*phi + (0.0034029))*pp + ((-1.5102e-04)*phi*phi + (-3.7038e-04)*phi + (0.0039502));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMM0][Sector 2] is:
                dp = dp +  ((1.2958e-07)*phi*phi +  (1.8668e-05)*phi + (-9.8427e-04))*pp*pp + ((-8.5802e-07)*phi*phi + (-2.1932e-04)*phi +  (0.010179))*pp +  ((1.0415e-05)*phi*phi +  (6.0621e-04)*phi + (-0.022855));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMM0][Sector 3] is:
                dp = dp +  ((1.5481e-06)*phi*phi + (-1.4515e-05)*phi + (-9.3973e-04))*pp*pp + ((-1.9977e-05)*phi*phi +  (2.1700e-04)*phi + (0.0088174))*pp +  ((5.7990e-05)*phi*phi + (-6.8656e-04)*phi + (-0.014188));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMM0][Sector 4] is:
                dp = dp +  ((5.4328e-06)*phi*phi +  (2.2980e-05)*phi +  (-0.0010726))*pp*pp + ((-6.7834e-05)*phi*phi + (-3.1792e-04)*phi +   (0.01149))*pp +  ((1.8968e-04)*phi*phi +  (9.9619e-04)*phi + (-0.023818));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMM0][Sector 5] is:
                dp = dp + ((-2.0199e-06)*phi*phi +  (1.7057e-05)*phi + (-4.7316e-04))*pp*pp +  ((3.4755e-05)*phi*phi + (-2.3546e-04)*phi + (0.0041369))*pp + ((-1.3950e-04)*phi*phi +  (8.7172e-04)*phi + (-0.0032131));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMM0][Sector 6] is:
                dp = dp + ((-2.7520e-06)*phi*phi + (-6.1071e-06)*phi + (-7.9342e-04))*pp*pp +  ((4.8167e-05)*phi*phi +  (9.1905e-05)*phi + (0.0072465))*pp + ((-1.9332e-04)*phi*phi + (-1.6235e-04)*phi + (-0.011128));
            }

            // Refinement Made on 7/25/2024 (after the Second Refinement of 'PipMMfaP2')
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMMfaP2][Sector 1] is:
                dp = dp +  ((3.6749e-06)*phi*phi +  (2.3529e-05)*phi + (-4.5740e-04))*pp*pp + ((-5.2483e-05)*phi*phi + (-3.5286e-04)*phi +   (0.006977))*pp +  ((1.7085e-04)*phi*phi +   (0.0012991)*phi + (-0.018722));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMMfaP2][Sector 2] is:
                dp = dp +  ((2.2726e-06)*phi*phi +  (4.4338e-06)*phi +  (3.0592e-04))*pp*pp + ((-2.3321e-05)*phi*phi + (-8.5568e-05)*phi + (-0.0034316))*pp +  ((3.6434e-05)*phi*phi +  (4.5930e-04)*phi + (0.012294));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMMfaP2][Sector 3] is:
                dp = dp + ((-1.1740e-06)*phi*phi +  (1.3492e-05)*phi +  (2.8583e-04))*pp*pp +  ((1.2246e-05)*phi*phi + (-1.5639e-04)*phi + (-0.0012797))*pp + ((-2.0712e-05)*phi*phi +  (4.6236e-04)*phi + (-0.0031846));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMMfaP2][Sector 4] is:
                dp = dp + ((-5.0081e-06)*phi*phi + (-2.9589e-05)*phi +   (0.0013289))*pp*pp +  ((7.1209e-05)*phi*phi +  (4.3696e-04)*phi +  (-0.015501))*pp + ((-2.1883e-04)*phi*phi +  (-0.0015507)*phi + (0.037174));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMMfaP2][Sector 5] is:
                dp = dp +  ((6.2698e-06)*phi*phi +  (2.4595e-05)*phi + (-3.4384e-04))*pp*pp + ((-8.5344e-05)*phi*phi + (-3.0910e-04)*phi +  (0.0059372))*pp +  ((2.6518e-04)*phi*phi +  (7.1389e-04)*phi + (-0.023712));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMMfaP2][Sector 6] is:
                dp = dp +  ((3.1397e-06)*phi*phi + (-6.5525e-06)*phi +  (6.5432e-04))*pp*pp + ((-3.9843e-05)*phi*phi +  (7.6638e-05)*phi +   (-0.00657))*pp +  ((1.1039e-04)*phi*phi + (-8.5754e-05)*phi + (0.011135));
            }
            
            // Refinement Made on 7/26/2024 (after the Refinement above but without the pion correction)
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMM0][Sector 1] is:
                dp = dp + ((-2.2791e-06)*phi*phi + (-6.1488e-06)*phi +  (3.8575e-04))*pp*pp +  ((3.0046e-05)*phi*phi +  (1.1854e-04)*phi +  (-0.0051974))*pp + ((-9.5549e-05)*phi*phi + (-6.0289e-04)*phi +  (0.010494));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMM0][Sector 2] is:
                dp = dp +  ((8.4441e-07)*phi*phi +  (8.6087e-06)*phi + (-5.1934e-04))*pp*pp + ((-1.5681e-05)*phi*phi + (-8.1106e-05)*phi +   (0.0063599))*pp +  ((7.9405e-05)*phi*phi + (-2.2007e-05)*phi + (-0.022475));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMM0][Sector 3] is:
                dp = dp +  ((5.5660e-08)*phi*phi +  (1.8715e-05)*phi + (-5.2988e-04))*pp*pp +  ((3.8227e-06)*phi*phi + (-2.6868e-04)*phi +   (0.0044237))*pp + ((-2.7981e-05)*phi*phi +  (8.5807e-04)*phi + (-0.0064594));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMM0][Sector 4] is:
                dp = dp +  ((2.8425e-06)*phi*phi + (2.8509e-05)*phi +   (-0.0011485))*pp*pp + ((-3.8444e-05)*phi*phi + (-4.1465e-04)*phi +    (0.013079))*pp +  ((1.0860e-04)*phi*phi +   (0.0014329)*phi + (-0.029556));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMM0][Sector 5] is:
                dp = dp + ((-2.3023e-06)*phi*phi + (-9.7500e-06)*phi + (-8.4870e-05))*pp*pp +  ((3.2564e-05)*phi*phi +  (1.5353e-04)*phi + (-2.7112e-04))*pp + ((-1.0867e-04)*phi*phi + (-3.8889e-04)*phi +  (0.0075836));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMM0][Sector 6] is:
                dp = dp +  ((5.6403e-07)*phi*phi +  (9.4142e-06)*phi + (-6.6549e-04))*pp*pp + ((-9.0669e-06)*phi*phi + (-8.7099e-05)*phi +   (0.0066379))*pp +  ((4.2643e-05)*phi*phi +  (1.7233e-05)*phi + (-0.011017));
            }
            
            // Refinement Made on 7/31/2024 (after the Refinement above but without the pion momentum OR energy loss corrections)
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 1] is:
                dp = dp + ((-2.9118e-07)*phi*phi + (-3.8417e-06)*phi +  (2.6829e-04))*pp*pp +  ((2.5593e-06)*phi*phi +  (4.7460e-05)*phi +    (0.003023))*pp + ((-2.3706e-06)*phi*phi + (-5.4818e-05)*phi + (-0.035521));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 2] is:
                dp = dp + ((-1.7109e-06)*phi*phi + (-1.2492e-05)*phi +  (9.4360e-04))*pp*pp +  ((2.5471e-05)*phi*phi +  (1.9015e-04)*phi +  (-0.0041101))*pp + ((-8.6916e-05)*phi*phi + (-5.3564e-04)*phi + (-0.021245));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 3] is:
                dp = dp + ((-8.9778e-07)*phi*phi + (-2.3087e-05)*phi +  (8.3325e-04))*pp*pp +  ((4.0377e-06)*phi*phi +  (3.0173e-04)*phi +  (-0.0015975))*pp +  ((2.3412e-05)*phi*phi + (-8.9876e-04)*phi + (-0.031861));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 4] is:
                dp = dp + ((-2.1736e-07)*phi*phi + (-5.6542e-06)*phi +  (6.6485e-04))*pp*pp +  ((9.6097e-07)*phi*phi +  (1.0747e-04)*phi + (-7.7464e-04))*pp +  ((1.4634e-06)*phi*phi + (-5.3925e-04)*phi + (-0.029181));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 5] is:
                dp = dp + ((-3.5487e-06)*phi*phi + (-1.2765e-05)*phi +   (0.0012549))*pp*pp +  ((4.5289e-05)*phi*phi +  (1.9156e-04)*phi +  (-0.0064094))*pp + ((-1.2323e-04)*phi*phi + (-8.2104e-04)*phi + (-0.030439));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 6] is:
                dp = dp + ((-3.3286e-06)*phi*phi +  (1.4953e-05)*phi +    (0.001376))*pp*pp +  ((5.0819e-05)*phi*phi + (-2.7514e-04)*phi +  (-0.0089155))*pp + ((-1.7831e-04)*phi*phi +   (0.0012799)*phi + (-0.019473));
            }
            
            // Refinement Made on 8/6/2024 (after the Refinement above but without the pion momentum OR energy loss corrections)
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 1] is:
                dp = dp + ((-6.6249e-06)*phi*phi + (-7.1308e-06)*phi +  (9.0366e-04))*pp*pp +  ((8.9977e-05)*phi*phi +  (9.1213e-05)*phi +  (-0.011119))*pp + ((-2.7393e-04)*phi*phi + (-2.6616e-04)*phi +   (0.030305));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 2] is:
                dp = dp + ((-4.8009e-06)*phi*phi + (-1.7873e-05)*phi +  (6.0431e-04))*pp*pp +  ((6.6262e-05)*phi*phi +  (2.4353e-04)*phi + (-0.0077579))*pp + ((-2.1419e-04)*phi*phi + (-7.4896e-04)*phi +   (0.022639));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 3] is:
                dp = dp + ((-9.3764e-07)*phi*phi + (-1.7400e-06)*phi + (-1.8600e-04))*pp*pp +  ((1.4379e-05)*phi*phi +  (5.3083e-06)*phi +  (0.0028469))*pp + ((-4.8285e-05)*phi*phi +  (1.2835e-04)*phi +  (-0.009912));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 4] is:
                dp = dp + ((-1.4164e-06)*phi*phi + (-1.2799e-05)*phi +  (2.6581e-04))*pp*pp +  ((1.8777e-05)*phi*phi +  (1.6598e-04)*phi + (-0.0022073))*pp + ((-6.2354e-05)*phi*phi + (-5.1263e-04)*phi +  (0.0010122));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 5] is:
                dp = dp + ((-4.6181e-09)*phi*phi +  (3.4925e-05)*phi +  (3.0517e-04))*pp*pp + ((-1.2550e-06)*phi*phi + (-4.5135e-04)*phi + (-0.0031892))*pp +  ((1.5709e-05)*phi*phi +   (0.0013502)*phi +  (0.0047851));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 6] is:
                dp = dp + ((-1.1158e-06)*phi*phi + (-3.5765e-05)*phi +  (6.0873e-04))*pp*pp +  ((1.2177e-05)*phi*phi +  (4.9330e-04)*phi + (-0.0066394))*pp + ((-2.1823e-05)*phi*phi +  (-0.0014821)*phi +   (0.012634));
            }
            
            // Refinement Made on 8/7/2024 (after the Refinement above but without the pion momentum OR energy loss corrections)
            // Refinement split into two parts for lower and higher electron momentum events (the ∆P plots were easier to fit with this split)
            if(((sec == 1 || sec == 2 || sec == 4) && pp < 6.5) || ((sec == 3 || sec == 5 || sec == 6) && pp < 4.75)){
                if(sec == 1){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 1] is:
                    dp = dp + ((-3.5875e-06)*phi*phi +  (1.1440e-04)*phi + (-0.0013413))*pp*pp + ((-1.4493e-05)*phi*phi +  (-0.0010658)*phi +   (0.015684))*pp +  ((1.3927e-04)*phi*phi +   (0.0022719)*phi +  (-0.038484));
                }
                if(sec == 2){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 2] is:
                    dp = dp +  ((1.2442e-05)*phi*phi + (-6.1576e-05)*phi +  (0.0010441))*pp*pp + ((-1.4122e-04)*phi*phi +  (5.0119e-04)*phi + (-0.0066685))*pp +  ((3.7700e-04)*phi*phi + (-8.6600e-04)*phi +  (0.0037052));
                }
                if(sec == 3){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 3] is:
                    dp = dp +  ((2.9798e-05)*phi*phi + (-6.2435e-04)*phi + (-0.0043415))*pp*pp + ((-2.4354e-04)*phi*phi +   (0.0045647)*phi +   (0.029557))*pp +  ((4.7502e-04)*phi*phi +  (-0.0080329)*phi +  (-0.047938));
                }
                if(sec == 4){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 4] is:
                    dp = dp + ((-3.8057e-06)*phi*phi + (-1.1953e-04)*phi +  (0.0018741))*pp*pp +  ((4.7549e-05)*phi*phi +   (0.0010643)*phi +  (-0.018171))*pp + ((-1.0543e-04)*phi*phi +  (-0.0022299)*phi +   (0.040794));
                }
                if(sec == 5){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 5] is:
                    dp = dp + ((-7.3697e-05)*phi*phi + (-9.7192e-04)*phi +  (0.0092912))*pp*pp +  ((5.4180e-04)*phi*phi +   (0.0069759)*phi +  (-0.073704))*pp + ((-9.5172e-04)*phi*phi +   (-0.011792)*phi +    (0.13433));
                }
                if(sec == 6){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 6] is:
                    dp = dp +  ((1.6536e-05)*phi*phi + (-2.5969e-04)*phi +  (0.0058283))*pp*pp + ((-1.4911e-04)*phi*phi +   (0.0017156)*phi +  (-0.040792))*pp +  ((3.1254e-04)*phi*phi +  (-0.0026549)*phi +   (0.067297));
                }
            }
            else{ // For higher momentum electron refinements
                if(sec == 1){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 1] is:
                    dp = dp +  ((4.1348e-06)*phi*phi + (-1.0315e-05)*phi + (-0.0071346))*pp*pp + ((-6.2846e-05)*phi*phi +  (1.5564e-04)*phi +    (0.11674))*pp +  ((2.3373e-04)*phi*phi + (-5.4842e-04)*phi +   (-0.47101));
                }
                if(sec == 2){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 2] is:
                    dp = dp +  ((5.3321e-06)*phi*phi +  (6.5264e-05)*phi + (-0.0063779))*pp*pp + ((-9.0979e-05)*phi*phi +  (-0.0010132)*phi +     (0.1008))*pp +  ((3.8553e-04)*phi*phi +   (0.0038941)*phi +   (-0.38978));
                }
                if(sec == 3){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 3] is:
                    dp = dp +  ((4.4168e-06)*phi*phi + (-3.2397e-05)*phi + (-0.0021061))*pp*pp + ((-7.3017e-05)*phi*phi +  (6.0511e-04)*phi +   (0.032786))*pp +  ((2.9350e-04)*phi*phi +  (-0.0027302)*phi +   (-0.12387));
                }
                if(sec == 4){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 4] is:
                    dp = dp +  ((1.5535e-05)*phi*phi +  (1.5075e-05)*phi + (-0.0067884))*pp*pp + ((-2.6185e-04)*phi*phi + (-2.2373e-04)*phi +    (0.10851))*pp +   ((0.0010982)*phi*phi +  (8.2408e-04)*phi +   (-0.42621));
                }
                if(sec == 5){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 5] is:
                    dp = dp + ((-4.2014e-06)*phi*phi +  (1.5447e-05)*phi + (-0.0016463))*pp*pp +  ((6.9456e-05)*phi*phi + (-1.4640e-04)*phi +   (0.022066))*pp + ((-2.7748e-04)*phi*phi +  (1.9352e-04)*phi +  (-0.066865));
                }
                if(sec == 6){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 6] is:
                    dp = dp + ((-1.1300e-06)*phi*phi +  (1.1866e-05)*phi + (-0.0014003))*pp*pp +  ((1.8917e-05)*phi*phi + (-1.0871e-04)*phi +   (0.018169))*pp + ((-8.2099e-05)*phi*phi +  (8.0667e-05)*phi +  (-0.051481));
                }
            }

            // Refinement Made on 8/7/2024 (after the Refinement above but without the pion momentum OR energy loss corrections)
            // Refined again with the same split as above (it should be possible to condense these split corrections into one refinement later)
            if(((sec == 1 || sec == 2 || sec == 4) && pp < 6.5) || ((sec == 3 || sec == 5 || sec == 6) && pp < 4.75)){
                if(sec == 1){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 1] is:
                    dp = dp + ((-8.2394e-06)*phi*phi + (-1.4770e-04)*phi +   (0.0015837))*pp*pp +  ((9.9903e-05)*phi*phi +   (0.0012864)*phi +  (-0.015075))*pp + ((-2.6728e-04)*phi*phi +  (-0.0024798)*phi +  (0.031067));
                }
                if(sec == 2){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 2] is:
                    dp = dp +  ((1.7611e-06)*phi*phi +  (1.8503e-05)*phi +   (-0.002415))*pp*pp +  ((4.4876e-06)*phi*phi + (-1.8341e-04)*phi +   (0.019642))*pp + ((-5.6153e-05)*phi*phi +  (3.7776e-04)*phi +  (-0.03365));
                }
                if(sec == 3){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 3] is:
                    dp = dp + ((-7.0833e-05)*phi*phi +  (2.7438e-04)*phi +   (0.0081054))*pp*pp +  ((5.2013e-04)*phi*phi +  (-0.0019764)*phi +  (-0.056939))*pp + ((-9.1842e-04)*phi*phi +   (0.0032572)*phi +  (0.097675));
                }
                if(sec == 4){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 4] is:
                    dp = dp +  ((8.1610e-06)*phi*phi +  (6.6565e-05)*phi +   (-0.001335))*pp*pp + ((-7.8258e-05)*phi*phi + (-5.9657e-04)*phi +   (0.010906))*pp +  ((1.3074e-04)*phi*phi +    (0.001168)*phi + (-0.018481));
                }
                if(sec == 5){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 5] is:
                    dp = dp + ((-2.2797e-05)*phi*phi +  (4.5663e-04)*phi +   (0.0064275))*pp*pp +  ((9.4699e-05)*phi*phi +  (-0.0034621)*phi +  (-0.035469))*pp + ((-3.0126e-05)*phi*phi +   (0.0060093)*phi +  (0.039262));
                }
                if(sec == 6){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 6] is:
                    dp = dp +  ((3.6702e-05)*phi*phi + (-8.9267e-05)*phi +   (-0.010563))*pp*pp + ((-2.8588e-04)*phi*phi +  (6.9722e-04)*phi +   (0.078616))*pp +  ((5.3578e-04)*phi*phi +  (-0.0011569)*phi +  (-0.13956));
                }
            }
            else{ // For higher momentum electron refinements
                if(sec == 1){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 1] is:
                    dp = dp + ((-5.3051e-06)*phi*phi + (-8.8354e-05)*phi +   (0.0042506))*pp*pp +  ((8.8756e-05)*phi*phi +   (0.0015399)*phi +  (-0.071353))*pp + ((-3.5658e-04)*phi*phi +  (-0.0065545)*phi +   (0.29204));
                }
                if(sec == 2){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 2] is:
                    dp = dp + ((-1.2703e-05)*phi*phi + (-3.5027e-05)*phi +  (8.1537e-04))*pp*pp +  ((1.8912e-04)*phi*phi +  (5.8533e-04)*phi +  (-0.010867))*pp + ((-6.7757e-04)*phi*phi +  (-0.0025099)*phi +  (0.033958));
                }
                if(sec == 3){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 3] is:
                    dp = dp +  ((3.6457e-06)*phi*phi +  (1.6952e-05)*phi + (-2.4470e-05))*pp*pp + ((-4.2257e-05)*phi*phi + (-3.6667e-04)*phi + (-0.0013049))*pp +  ((8.8870e-05)*phi*phi +   (0.0018652)*phi +  (0.013666));
                }
                if(sec == 4){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 4] is:
                    dp = dp + ((-3.2511e-05)*phi*phi +  (9.8205e-05)*phi +   (0.0035782))*pp*pp +  ((5.3907e-04)*phi*phi +  (-0.0017016)*phi +  (-0.057211))*pp +   ((-0.002202)*phi*phi +   (0.0072935)*phi +   (0.22406));
                }
                if(sec == 5){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 5] is:
                    dp = dp +  ((5.5197e-06)*phi*phi +  (4.1665e-05)*phi +  (-0.0010277))*pp*pp + ((-8.6190e-05)*phi*phi + (-7.1269e-04)*phi +   (0.017472))*pp +  ((3.3233e-04)*phi*phi +   (0.0029846)*phi + (-0.073686));
                }
                if(sec == 6){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 6] is:
                    dp = dp + ((-1.5585e-06)*phi*phi +  (2.5187e-06)*phi + (-5.3017e-04))*pp*pp +  ((2.1413e-05)*phi*phi + (-4.9446e-05)*phi +   (0.010779))*pp + ((-6.5129e-05)*phi*phi +  (2.0750e-04)*phi + (-0.053002));
                }
            }
            
            // Refinement Made on 8/8/2024 (after the Refinements above without the pion momentum OR energy loss corrections)
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 1] is:
                dp = dp +  ((5.6395e-06)*phi*phi +  (3.5179e-06)*phi + (-3.6014e-04))*pp*pp + ((-7.7355e-05)*phi*phi + (-4.2292e-05)*phi +  (0.0058671))*pp +  ((2.3853e-04)*phi*phi +  (7.8729e-05)*phi +   (-0.018028));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 2] is:
                dp = dp +  ((1.5380e-06)*phi*phi +  (1.7542e-07)*phi +  (1.4941e-04))*pp*pp + ((-2.1330e-05)*phi*phi + (-5.0463e-05)*phi + (-0.0015399))*pp +  ((5.1566e-05)*phi*phi +  (4.0322e-04)*phi +   (0.0031053));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 3] is:
                dp = dp + ((-1.2290e-06)*phi*phi +  (3.8490e-05)*phi +  (2.3519e-04))*pp*pp +  ((1.7922e-05)*phi*phi + (-5.2472e-04)*phi +  (-0.003093))*pp + ((-5.4184e-05)*phi*phi +   (0.0016244)*phi +   (0.0080313));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 4] is:
                dp = dp +  ((3.3920e-07)*phi*phi +  (1.4318e-05)*phi + (-5.4906e-04))*pp*pp + ((-1.7911e-05)*phi*phi + (-1.7201e-04)*phi +  (0.0079316))*pp +  ((1.1164e-04)*phi*phi +  (4.0432e-04)*phi +   (-0.024017));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 5] is:
                dp = dp +  ((3.9633e-06)*phi*phi +  (4.9717e-06)*phi + (-5.7672e-04))*pp*pp + ((-4.9436e-05)*phi*phi + (-5.7359e-05)*phi +  (0.0069029))*pp +  ((1.2605e-04)*phi*phi +  (8.6844e-05)*phi +   (-0.014798));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 6] is:
                dp = dp + ((-3.1884e-06)*phi*phi + (-2.3096e-06)*phi + (-2.4516e-04))*pp*pp +  ((4.3662e-05)*phi*phi +  (3.4307e-05)*phi +  (0.0023136))*pp + ((-1.4949e-04)*phi*phi + (-9.5104e-05)*phi +  (9.7470e-05));
            }
            
            
            // Refinement Made on 8/8/2024 (after the Refinements above without the pion momentum OR energy loss corrections)
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 1] is:
                dp = dp + ((-3.1299e-06)*phi*phi + (-9.0571e-06)*phi +  (5.1829e-04))*pp*pp +  ((4.9000e-05)*phi*phi +  (7.0257e-05)*phi + (-0.0077222))*pp + ((-1.8050e-04)*phi*phi +  (4.6552e-05)*phi +   (0.024068));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 2] is:
                dp = dp + ((-4.5509e-06)*phi*phi +  (6.3454e-06)*phi +  (9.9070e-05))*pp*pp +  ((5.3758e-05)*phi*phi + (-1.4417e-05)*phi + (-0.0010708))*pp + ((-1.2940e-04)*phi*phi + (-3.4349e-04)*phi +  (0.0025952));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 3] is:
                dp = dp +  ((2.0979e-06)*phi*phi + (-3.4180e-05)*phi + (-1.2768e-04))*pp*pp + ((-2.7155e-05)*phi*phi +  (4.4784e-04)*phi +  (0.0014403))*pp +  ((8.0524e-05)*phi*phi +   (-0.001275)*phi + (-0.0024191));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 4] is:
                dp = dp + ((-4.0095e-06)*phi*phi +  (1.0225e-06)*phi +  (8.4345e-04))*pp*pp +  ((5.8392e-05)*phi*phi + (-4.8236e-05)*phi +  (-0.011577))*pp + ((-1.9024e-04)*phi*phi +  (3.7387e-04)*phi +   (0.032263));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 5] is:
                dp = dp + ((-3.9318e-06)*phi*phi + (-1.5812e-06)*phi +  (3.7381e-04))*pp*pp +  ((4.8262e-05)*phi*phi +  (1.6128e-05)*phi + (-0.0041772))*pp + ((-1.2398e-04)*phi*phi + (-8.1429e-06)*phi +  (0.0080694));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2][Sector 6] is:
                dp = dp + ((-1.1601e-06)*phi*phi +  (1.7698e-05)*phi +  (5.2596e-04))*pp*pp +  ((8.4153e-06)*phi*phi + (-2.4553e-04)*phi + (-0.0064071))*pp +  ((1.6811e-05)*phi*phi +  (7.8649e-04)*phi +   (0.013265));
            }
            
            // Refinement Made on 8/15/2024 (after the all Refinements, including pion momentum and energy loss corrections)
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMMfaP2][Sector 1] is:
                dp = dp + ((2.3137e-06)*phi*phi + (-4.8175e-06)*phi + (-5.2636e-04))*pp*pp + ((-4.3444e-05)*phi*phi + (8.5040e-05)*phi + (0.007777))*pp + ((1.8592e-04)*phi*phi + (-3.5029e-04)*phi + (-0.026094));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMMfaP2][Sector 2] is:
                dp = dp + ((2.8942e-06)*phi*phi + (8.1917e-07)*phi + (-6.3981e-04))*pp*pp + ((-3.6146e-05)*phi*phi + (-7.2120e-05)*phi + (0.0055736))*pp + ((9.5562e-05)*phi*phi + (5.0736e-04)*phi + (-0.0062031));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMMfaP2][Sector 3] is:
                dp = dp + ((2.1858e-06)*phi*phi + (1.4685e-05)*phi + (-1.3021e-04))*pp*pp + ((-2.4808e-05)*phi*phi + (-1.7955e-04)*phi + (8.8710e-05))*pp + ((5.4301e-05)*phi*phi + (3.1788e-04)*phi + (0.0026921));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMMfaP2][Sector 4] is:
                dp = dp + ((5.1042e-06)*phi*phi + (-1.1875e-05)*phi + (-6.0586e-04))*pp*pp + ((-6.7165e-05)*phi*phi + (1.4061e-04)*phi + (0.0072229))*pp + ((1.9008e-04)*phi*phi + (-2.8607e-04)*phi + (-0.020165));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMMfaP2][Sector 5] is:
                dp = dp + ((1.6874e-06)*phi*phi + (4.5833e-08)*phi + (-3.3929e-04))*pp*pp + ((-1.8054e-05)*phi*phi + (-2.2540e-05)*phi + (0.0016773))*pp + ((2.7613e-05)*phi*phi + (2.8337e-05)*phi + (0.0061736));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmfaP2_ELPipMMfaP2][Sector 6] is:
                dp = dp + ((7.7618e-07)*phi*phi + (4.6542e-06)*phi + (-7.1218e-04))*pp*pp + ((-1.0952e-05)*phi*phi + (-1.5113e-06)*phi + (0.0087942))*pp + ((3.0599e-05)*phi*phi + (-3.4246e-04)*phi + (-0.022545));
            }
            
        }

    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //====================================================================================================================================//
    //======================//======================//     Electron Corrections (End)     //======================//======================//
    //====================================================================================================================================//
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
    
    
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //====================================================================================================================================//
    //=========================//=========================//     π+ Corrections     //=========================//=========================//
    //====================================================================================================================================//
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    if(ivec == 1 && corPip != 0){
        // Old Corrections (PipMMF)
        if(sec == 1){
            dp = ((5.7e-07)*phi*phi + (-2.531e-05)*phi + (3.2253e-04))*pp*pp + ((2.12e-06)*phi*phi + (-3.6741e-04)*phi + (-0.01378))*pp + ((-1.215e-05)*phi*phi + (4.275e-04)*phi + (0.04561));
            dp = dp + ((-2.12e-06)*phi*phi + (3.185e-05)*phi + (0.00178389))*pp*pp + ((1.262e-05)*phi*phi + (-0.00012324)*phi + (-0.01494883))*pp + ((-1.422e-05)*phi*phi + (0.00021045)*phi + (0.02590949));
        }
        if(sec == 2){
            dp = ((-4e-08)*phi*phi + (-9.836e-05)*phi + (3.142e-04))*pp*pp + ((8.6e-07)*phi*phi + (4.6073e-04)*phi + (-0.0136))*pp + ((8.09e-06)*phi*phi + (-6.0253e-04)*phi + (0.03594));
            dp = dp + ((-9.8e-07)*phi*phi + (3.974e-05)*phi + (0.00159441))*pp*pp + ((6.61e-06)*phi*phi + (-0.00023934)*phi + (-0.01295355))*pp + ((-1.087e-05)*phi*phi + (0.00027704)*phi + (0.02013232));
        }
        if(sec == 3){
            dp = ((-1.37e-06)*phi*phi + (3.759e-05)*phi + (7.4895e-04))*pp*pp + ((8.45e-06)*phi*phi + (1.464e-04)*phi + (-0.01952))*pp + ((-1.41e-06)*phi*phi + (-3.5781e-04)*phi + (0.0353));
            dp = dp + ((-3.2e-07)*phi*phi + (-2.98e-06)*phi + (0.00144252))*pp*pp + ((2.9e-06)*phi*phi + (-5.719e-05)*phi + (-0.01197579))*pp + ((-5.74e-06)*phi*phi + (0.00024614)*phi + (0.02228774));
        }
        if(sec == 4){
            dp = ((2.7e-06)*phi*phi + (5.028e-05)*phi + (9.007e-04))*pp*pp + ((-1.548e-05)*phi*phi + (-6.141e-05)*phi + (-0.0151))*pp + ((2.063e-05)*phi*phi + (1.7882e-04)*phi + (0.03522));
            dp = dp + ((-8.2e-07)*phi*phi + (-2.606e-05)*phi + (0.00102121))*pp*pp + ((6.32e-06)*phi*phi + (0.00013252)*phi + (-0.00898872))*pp + ((-9.79e-06)*phi*phi + (-0.00017861)*phi + (0.01654247));
        }
        if(sec == 5){
            dp = ((2.2e-06)*phi*phi + (-1.554e-05)*phi + (5.465e-04))*pp*pp + ((-1.06e-05)*phi*phi + (1.226e-04)*phi + (-0.01651))*pp + ((1.039e-05)*phi*phi + (-2.062e-04)*phi + (0.0436));
            dp = dp + ((-5.8e-07)*phi*phi + (-1.4e-07)*phi + (0.00129068))*pp*pp + ((5.43e-06)*phi*phi + (-2.262e-05)*phi + (-0.01076443))*pp + ((-7.78e-06)*phi*phi + (0.00010021)*phi + (0.01975448));
        }
        if(sec == 6){
            dp = ((1.11e-06)*phi*phi + (-1e-08)*phi + (6.88e-05))*pp*pp + ((-8.86e-06)*phi*phi + (-5.94e-05)*phi + (-0.01133))*pp + ((1.919e-05)*phi*phi + (-2.444e-04)*phi + (0.03491));
            dp = dp + ((-1.15e-06)*phi*phi + (6.34e-06)*phi + (0.00196799))*pp*pp + ((1.196e-05)*phi*phi + (-0.00010685)*phi + (-0.01774286))*pp + ((-2.573e-05)*phi*phi + (0.00042626)*phi + (0.03688378));
        }

        // Extended Corrections Test (PipMMExF)
        if(corPip == 2){
            if(sec == 1){
                dp =      ((-5.5619e-07)*phi*phi +  (1.2176e-05)*phi +   (0.0019766))*pp*pp +  ((2.2974e-06)*phi*phi + (-3.2344e-04)*phi +  (-0.018279))*pp + ((-3.3287e-06)*phi*phi +  (1.2371e-04)*phi + (0.037557));
                dp = dp + ((-1.1071e-07)*phi*phi +  (1.1611e-05)*phi + (-6.8815e-04))*pp*pp + ((-2.2037e-06)*phi*phi + (-1.8548e-04)*phi +  (0.0055018))*pp +  ((2.3393e-07)*phi*phi +  (1.2655e-04)*phi + (-0.0055127));
                dp = dp + ((-1.0665e-06)*phi*phi + (-9.2758e-06)*phi +  (2.1876e-04))*pp*pp +  ((6.5297e-06)*phi*phi +  (2.7729e-05)*phi + (-0.0010923))*pp + ((-1.4148e-07)*phi*phi +  (2.9491e-05)*phi + (-0.0043183));
            }
            if(sec == 2){
                dp =      ((-3.0769e-06)*phi*phi +  (5.2387e-06)*phi +   (0.0025674))*pp*pp +  ((1.8124e-05)*phi*phi + (-1.7621e-04)*phi +  (-0.020154))*pp + ((-1.2558e-05)*phi*phi +  (1.2769e-04)*phi + (0.033566));
                dp = dp + ((-1.2998e-06)*phi*phi + (-2.7296e-05)*phi + (-1.2792e-04))*pp*pp +  ((6.8931e-06)*phi*phi +  (1.6941e-04)*phi +  (0.0013802))*pp + ((-8.9689e-06)*phi*phi + (-2.5644e-04)*phi + (-0.0032964));
                dp = dp + ((-9.8764e-08)*phi*phi + (-1.9100e-05)*phi + (-3.9391e-04))*pp*pp + ((-3.3432e-07)*phi*phi +  (1.0039e-04)*phi +  (0.0033748))*pp +  ((5.3722e-06)*phi*phi + (-1.1331e-04)*phi + (-0.0070953));
            }
            if(sec == 3){
                dp =       ((1.3125e-06)*phi*phi + (-5.9180e-05)*phi +   (0.0014564))*pp*pp + ((-7.2451e-06)*phi*phi +  (6.3174e-04)*phi +  (-0.017146))*pp +  ((1.0599e-05)*phi*phi + (-8.1889e-04)*phi + (0.029497));
                dp = dp + ((-1.7131e-06)*phi*phi +  (5.7922e-05)*phi +  (5.9580e-04))*pp*pp +  ((1.1049e-05)*phi*phi + (-2.7280e-04)*phi + (-0.0039213))*pp + ((-8.5944e-06)*phi*phi +  (2.8071e-04)*phi + (-1.3545e-04));
                dp = dp + ((-4.0314e-07)*phi*phi +  (4.1308e-06)*phi + (-5.3057e-04))*pp*pp +  ((1.3308e-06)*phi*phi +  (1.2769e-05)*phi +  (0.0044938))*pp +  ((2.0059e-06)*phi*phi +  (9.1931e-06)*phi + (-0.0076076));
            }
            if(sec == 4){
                dp =      ((-3.3265e-07)*phi*phi + (-3.0209e-05)*phi +    (0.001713))*pp*pp +  ((7.3058e-06)*phi*phi +  (3.1596e-04)*phi +  (-0.017057))*pp + ((-1.3587e-05)*phi*phi + (-2.3543e-04)*phi + (0.034361));
                dp = dp +  ((9.2471e-07)*phi*phi +  (7.2685e-06)*phi + (-1.4055e-05))*pp*pp + ((-8.2856e-06)*phi*phi +  (1.0956e-05)*phi +  (0.0013298))*pp +  ((1.1312e-05)*phi*phi + (-3.6642e-05)*phi + (-0.004602));
                dp = dp + ((-1.2205e-06)*phi*phi +  (1.4853e-05)*phi +  (2.6654e-04))*pp*pp +  ((8.0883e-06)*phi*phi + (-8.1258e-05)*phi + (-0.0017054))*pp + ((-6.7779e-06)*phi*phi + (-4.1304e-05)*phi + (0.0013179));
                dp = dp +  ((2.4054e-07)*phi*phi + (-3.9757e-05)*phi +  (3.5924e-04))*pp*pp + ((-3.0307e-07)*phi*phi +  (3.2370e-04)*phi + (-0.0024836))*pp + ((-3.9735e-06)*phi*phi + (-2.7823e-04)*phi + (9.4398e-04));
            }
            if(sec == 5){
                dp =       ((4.9522e-08)*phi*phi +  (1.6615e-06)*phi +   (0.0013238))*pp*pp + ((-7.7824e-07)*phi*phi + (-1.8424e-05)*phi +  (-0.013754))*pp +  ((6.2245e-06)*phi*phi +  (5.4907e-05)*phi + (0.027401));
                dp = dp +  ((8.9196e-08)*phi*phi + (-3.7341e-05)*phi +  (1.5161e-05))*pp*pp +  ((3.2196e-06)*phi*phi +  (3.1272e-04)*phi + (-0.0012442))*pp + ((-9.1313e-06)*phi*phi + (-5.1308e-04)*phi + (0.0042737));
                dp = dp +  ((2.0598e-06)*phi*phi +  (2.0426e-05)*phi + (-1.5120e-04))*pp*pp + ((-1.2444e-05)*phi*phi + (-1.3032e-04)*phi + (7.0147e-04))*pp +  ((1.2403e-05)*phi*phi +  (7.1482e-05)*phi + (-0.0013052));
            }
            if(sec == 6){
                dp =      ((-1.1641e-06)*phi*phi +  (3.6397e-05)*phi +   (0.0017669))*pp*pp +  ((1.2615e-05)*phi*phi + (-3.1012e-04)*phi +  (-0.018168))*pp + ((-1.9665e-05)*phi*phi +  (6.8981e-05)*phi + (0.038744));
                dp = dp + ((-4.7604e-08)*phi*phi + (-8.9182e-06)*phi + (-9.4440e-05))*pp*pp + ((-1.9801e-06)*phi*phi +  (2.6388e-05)*phi +  (0.0014914))*pp +  ((5.5219e-06)*phi*phi + (-9.8614e-05)*phi + (-0.0038784));
                dp = dp +  ((8.1876e-07)*phi*phi + (-1.2894e-05)*phi + (-4.6578e-04))*pp*pp + ((-6.8450e-06)*phi*phi +  (8.5513e-05)*phi +  (0.0035454))*pp +  ((1.0147e-05)*phi*phi + (-1.0325e-04)*phi + (-0.0054159));
            }
        }

        // Final (Refined) Extended Corrections (PipMMEF)
        if(corPip == 3){
            if(sec == 1){
                dp =   ((-1.7334e-06)*phi*phi +  (1.45112e-05)*phi +  (0.00150721))*pp*pp +    ((6.6234e-06)*phi*phi + (-4.81191e-04)*phi +  (-0.0138695))*pp + ((-3.23625e-06)*phi*phi +   (2.79751e-04)*phi + (0.027726));
            }
            if(sec == 2){
                dp = ((-4.475464e-06)*phi*phi + (-4.11573e-05)*phi +  (0.00204557))*pp*pp +  ((2.468278e-05)*phi*phi +   (9.3590e-05)*phi +   (-0.015399))*pp + ((-1.61547e-05)*phi*phi +   (-2.4206e-04)*phi + (0.0231743));
            }
            if(sec == 3){
                dp =   ((-8.0374e-07)*phi*phi +   (2.8728e-06)*phi +  (0.00152163))*pp*pp +    ((5.1347e-06)*phi*phi +  (3.71709e-04)*phi +  (-0.0165735))*pp +   ((4.0105e-06)*phi*phi + (-5.289869e-04)*phi + (0.02175395));
            }
            if(sec == 4){
                dp =   ((-3.8790e-07)*phi*phi + (-4.78445e-05)*phi + (0.002324725))*pp*pp +   ((6.80543e-06)*phi*phi +  (5.69358e-04)*phi +  (-0.0199162))*pp + ((-1.30264e-05)*phi*phi +  (-5.91606e-04)*phi + (0.03202088));
            }
            if(sec == 5){
                dp =  ((2.198518e-06)*phi*phi + (-1.52535e-05)*phi + (0.001187761))*pp*pp + ((-1.000264e-05)*phi*phi +  (1.63976e-04)*phi + (-0.01429673))*pp +   ((9.4962e-06)*phi*phi +  (-3.86691e-04)*phi + (0.0303695));
            }
            if(sec == 6){
                dp =  ((-3.92944e-07)*phi*phi +  (1.45848e-05)*phi +  (0.00120668))*pp*pp +    ((3.7899e-06)*phi*phi + (-1.98219e-04)*phi +  (-0.0131312))*pp +  ((-3.9961e-06)*phi*phi +  (-1.32883e-04)*phi + (0.0294497));
            }
        }
        
        // New (Fall 2018 Pass 2) Corrections (PipMMfaP2)
        if(corPip == 4){
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMM0][Sector 1] is:
                dp =  ((2.3948e-06)*phi*phi + (-2.3484e-05)*phi +  (-0.0011859))*pp*pp + ((-1.8518e-05)*phi*phi +  (3.9815e-04)*phi +   (0.013015))*pp +  ((3.1635e-05)*phi*phi + (-3.7151e-04)*phi + (-0.033741));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMM0][Sector 2] is:
                dp = ((-5.3424e-07)*phi*phi +  (1.8585e-05)*phi + (-7.5600e-06))*pp*pp +  ((6.1948e-06)*phi*phi + (-1.0862e-04)*phi + (4.3139e-04))*pp + ((-9.0969e-06)*phi*phi +  (3.2448e-04)*phi + (-0.0096819));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMM0][Sector 3] is:
                dp =  ((1.1717e-06)*phi*phi +  (4.4573e-05)*phi + (-1.1291e-04))*pp*pp + ((-2.8729e-06)*phi*phi + (-5.0081e-04)*phi +  (0.0031723))*pp + ((-7.6835e-06)*phi*phi +  (4.0446e-05)*phi + (-0.008636));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMM0][Sector 4] is:
                dp = ((-1.0300e-06)*phi*phi +  (1.7003e-06)*phi + (-3.0130e-04))*pp*pp +  ((3.7758e-06)*phi*phi + (-6.2429e-05)*phi +  (0.0040738))*pp +  ((1.8369e-06)*phi*phi + (-5.6374e-04)*phi + (-0.016014));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMM0][Sector 5] is:
                dp =  ((8.2207e-08)*phi*phi +  (5.3275e-06)*phi + (-8.5237e-04))*pp*pp + ((-3.4509e-06)*phi*phi + (-9.7381e-05)*phi +  (0.0094486))*pp +  ((1.0053e-05)*phi*phi +  (5.5861e-05)*phi + (-0.025943));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMM0][Sector 6] is:
                dp =  ((9.2205e-07)*phi*phi + (-6.0142e-06)*phi +  (-0.0011434))*pp*pp + ((-5.0324e-06)*phi*phi +  (1.8013e-04)*phi +   (0.011213))*pp +  ((8.9720e-06)*phi*phi + (-4.6304e-04)*phi + (-0.02685));
            }
            
            // Refinement Made on 7/24/2024
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 1] is:
                dp = dp + ((-1.7295e-07)*phi*phi +  (5.4358e-06)*phi + (0.0018833))*pp*pp +  ((4.7587e-06)*phi*phi + (-3.1517e-04)*phi + (-0.026724))*pp + ((-1.4069e-05)*phi*phi +  (4.1176e-04)*phi + (0.069979));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 2] is:
                dp = dp + ((-1.1231e-06)*phi*phi + (-3.5943e-05)*phi + (0.0017063))*pp*pp +  ((1.0443e-05)*phi*phi +  (1.3001e-04)*phi + (-0.024158))*pp + ((-1.5673e-05)*phi*phi + (-1.3298e-04)*phi + (0.053998));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 3] is:
                dp = dp +  ((2.8841e-07)*phi*phi +  (3.4008e-06)*phi + (0.0015254))*pp*pp + ((-3.6231e-06)*phi*phi +  (1.6835e-04)*phi + (-0.024956))*pp +  ((1.3835e-05)*phi*phi + (-1.4615e-04)*phi + (0.050437));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 4] is:
                dp = dp +  ((1.1766e-06)*phi*phi +  (1.6616e-05)*phi + (0.0014358))*pp*pp + ((-7.6512e-06)*phi*phi +  (2.0966e-05)*phi + (-0.019282))*pp +  ((7.7158e-06)*phi*phi + (-1.8920e-05)*phi + (0.046453));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 5] is:
                dp = dp +  ((1.0623e-06)*phi*phi +  (1.1267e-05)*phi + (0.0015475))*pp*pp + ((-6.0837e-06)*phi*phi + (-9.9701e-05)*phi + (-0.023658))*pp +  ((7.7563e-06)*phi*phi +  (1.4607e-04)*phi + (0.05843));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 6] is:
                dp = dp +  ((5.1565e-07)*phi*phi +  (6.8622e-06)*phi + (0.0016907))*pp*pp +  ((2.1299e-06)*phi*phi + (-1.2797e-04)*phi + (-0.026013))*pp + ((-1.1271e-05)*phi*phi +  (1.1640e-04)*phi + (0.069137));
            }
            
            // Second Refinement Made on 7/24/2024
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 1] is:
                dp = dp + ((-6.6590e-07)*phi*phi + (-1.4415e-05)*phi +  (2.6848e-04))*pp*pp +  ((8.2632e-06)*phi*phi +  (6.2751e-05)*phi + (-0.0034742))*pp + ((-1.8878e-05)*phi*phi + (-1.2501e-04)*phi + (0.0086071));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 2] is:
                dp = dp + ((-1.4082e-07)*phi*phi + (-6.0881e-06)*phi +  (3.1590e-05))*pp*pp +  ((6.4693e-07)*phi*phi + (-7.6764e-06)*phi + (-0.0012825))*pp + ((-1.3667e-06)*phi*phi + (-5.0419e-05)*phi + (0.0056828));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 3] is:
                dp = dp + ((-1.6591e-06)*phi*phi +  (1.6359e-05)*phi +  (3.8770e-04))*pp*pp +  ((1.6448e-05)*phi*phi + (-4.7142e-05)*phi + (-0.0044578))*pp + ((-2.1872e-05)*phi*phi + (-7.9778e-05)*phi + (0.0074436));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 4] is:
                dp = dp + ((-1.1527e-06)*phi*phi +  (1.6651e-05)*phi +  (4.6146e-04))*pp*pp +  ((1.1977e-05)*phi*phi + (-1.0161e-04)*phi + (-0.0050631))*pp + ((-1.9141e-05)*phi*phi +  (2.0872e-04)*phi + (0.010377));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 5] is:
                dp = dp + ((-1.0662e-07)*phi*phi + (-2.4309e-05)*phi +  (3.6845e-04))*pp*pp +  ((4.0962e-06)*phi*phi +  (1.7250e-04)*phi + (-0.0042618))*pp + ((-8.5468e-06)*phi*phi + (-2.0804e-04)*phi + (0.0087841));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 6] is:
                dp = dp +  ((8.4139e-07)*phi*phi + (-2.8656e-06)*phi +  (3.9611e-04))*pp*pp + ((-4.7497e-06)*phi*phi +  (2.6192e-05)*phi + (-0.0040928))*pp +  ((6.7168e-06)*phi*phi + (-9.0270e-05)*phi + (0.0076946));
            }
            
            // Third Refinement Made on 8/13/2024 (Made after electron refinements)
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 1] is:
                dp = dp + ((-4.3684e-07)*phi*phi + (-1.3095e-05)*phi + (-6.1274e-04))*pp*pp +  ((6.4815e-07)*phi*phi +  (7.3289e-05)*phi +   (0.012824))*pp +  ((9.3306e-06)*phi*phi + (-2.4068e-05)*phi + (-0.033728));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 2] is:
                dp = dp + ( (3.8722e-07)*phi*phi + (-8.4667e-06)*phi + (-8.2958e-04))*pp*pp + ((-3.7052e-06)*phi*phi +  (9.7132e-05)*phi +   (0.014258))*pp +  ((6.3672e-06)*phi*phi + (-8.6202e-05)*phi + (-0.031074));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 3] is:
                dp = dp +  ((1.1841e-06)*phi*phi + (-3.8028e-06)*phi +  (-0.0012954))*pp*pp + ((-9.3855e-06)*phi*phi +  (2.3547e-05)*phi +   (0.017576))*pp +  ((1.1915e-05)*phi*phi + (-2.7994e-05)*phi + (-0.030905));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 4] is:
                dp = dp + ((-9.9920e-07)*phi*phi +  (1.2269e-05)*phi + (-7.7873e-04))*pp*pp +  ((5.1407e-06)*phi*phi + (-6.6605e-05)*phi +   (0.012997))*pp + ((-3.2993e-06)*phi*phi + (-8.9990e-05)*phi + (-0.028582));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 5] is:
                dp = dp + ((-6.5201e-08)*phi*phi + (-6.0608e-06)*phi + (-5.4151e-04))*pp*pp +  ((7.3912e-07)*phi*phi +  (4.2848e-05)*phi +   (0.010961))*pp +  ((4.9087e-06)*phi*phi + (-1.6735e-04)*phi + (-0.029336));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 6] is:
                dp = dp + ((-3.7458e-07)*phi*phi +  (5.6803e-06)*phi + (-3.1625e-04))*pp*pp +  ((3.1827e-06)*phi*phi + (-4.2862e-05)*phi +  (0.0095016))*pp + ((-6.9661e-06)*phi*phi +  (2.3350e-05)*phi + (-0.027473));
            }
            
            // 4th Refinement Made on 8/14/2024 (split mom refinement)
            if(((sec == 1 || sec == 2 || sec == 3) && pp < 5) || ((sec == 4 || sec == 5 || sec == 6) && pp < 4.5)){
                if(sec == 1){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 1] is:
                    dp = dp +  ((2.9639e-06)*phi*phi + (-1.2731e-04)*phi +  (6.8325e-04))*pp*pp + ((-2.0769e-05)*phi*phi +  (6.8741e-04)*phi + (-0.0025813))*pp +   ((1.4977e-05)*phi*phi + (-6.5156e-04)*phi +  (0.0035485));
                }
                if(sec == 2){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 2] is:
                    dp = dp +  ((3.3582e-06)*phi*phi + (-1.6123e-04)*phi +   (0.0014661))*pp*pp + ((-1.7191e-05)*phi*phi +  (8.7685e-04)*phi + (-0.0076688))*pp +   ((1.9961e-05)*phi*phi + (-8.5011e-04)*phi +    (0.00578));
                }
                if(sec == 3){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 3] is:
                    dp = dp + ((-8.6830e-07)*phi*phi +  (5.9703e-05)*phi +   (0.0013032))*pp*pp +  ((6.0055e-06)*phi*phi + (-3.6019e-04)*phi + (-0.0062311))*pp +  ((-1.0980e-05)*phi*phi +  (4.6372e-04)*phi +  (0.0053207));
                }
                if(sec == 4){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 4] is:
                    dp = dp +  ((5.2229e-06)*phi*phi +  (1.9574e-04)*phi +  (2.2872e-04))*pp*pp + ((-2.3170e-05)*phi*phi + (-9.5521e-04)*phi + (-0.0034589))*pp +   ((1.5039e-05)*phi*phi +  (9.0872e-04)*phi +  (0.0051232));
                }
                if(sec == 5){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 5] is:
                    dp = dp + ((-5.8188e-06)*phi*phi +  (1.6693e-04)*phi +   (0.0010372))*pp*pp +  ((2.6977e-05)*phi*phi + (-7.0556e-04)*phi + (-0.0039761))*pp +  ((-2.8235e-05)*phi*phi +  (5.2835e-04)*phi +   (0.002592));
                }
                if(sec == 6){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 6] is:
                    dp = dp +  ((2.4397e-07)*phi*phi + (-5.3125e-06)*phi +  (-0.0016639))*pp*pp +  ((1.7518e-06)*phi*phi + (-7.1887e-05)*phi +  (0.0065102))*pp +   ((1.4443e-06)*phi*phi +  (1.1702e-04)*phi + (-0.0059638));
                }
            }
            else{ // For higher momentum pion refinements
                if(sec == 1){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 1] is:
                    dp = dp + ((-1.0211e-06)*phi*phi + (-1.2476e-04)*phi +  (-0.0016665))*pp*pp +  ((1.3635e-05)*phi*phi +   (0.0017859)*phi +   (0.017797))*pp +  ((-5.4549e-05)*phi*phi +  (-0.0061437)*phi +  (-0.039813));
                }
                if(sec == 2){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 2] is:
                    dp = dp +  ((7.2850e-06)*phi*phi +  (1.9919e-04)*phi +  (-0.0023838))*pp*pp + ((-9.4438e-05)*phi*phi +  (-0.0024354)*phi +   (0.029087))*pp +   ((2.9427e-04)*phi*phi +   (0.0071514)*phi +  (-0.079795));
                }
                if(sec == 3){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 3] is:
                    dp = dp + ((-4.2567e-06)*phi*phi +  (1.2239e-04)*phi +  (-0.0023899))*pp*pp +  ((4.4797e-05)*phi*phi +  (-0.0016063)*phi +   (0.028418))*pp +  ((-1.2146e-04)*phi*phi +   (0.0050973)*phi +  (-0.074403));
                }
                if(sec == 4){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 4] is:
                    dp = dp + ((-2.5188e-06)*phi*phi +  (5.6253e-05)*phi +  (-0.0031624))*pp*pp +  ((2.8721e-05)*phi*phi + (-7.7158e-04)*phi +   (0.037865))*pp +  ((-7.2393e-05)*phi*phi +   (0.0025854)*phi +   (-0.10784));
                }
                if(sec == 5){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 5] is:
                    dp = dp +  ((3.9910e-06)*phi*phi +  (1.1435e-04)*phi +  (-0.0022152))*pp*pp + ((-4.6227e-05)*phi*phi +  (-0.0013773)*phi +   (0.026904))*pp +   ((1.1754e-04)*phi*phi +   (0.0041633)*phi +  (-0.073689));
                }
                if(sec == 6){
                    // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 6] is:
                    dp = dp +  ((2.0755e-06)*phi*phi + (-1.4409e-04)*phi +  (2.8350e-05))*pp*pp + ((-2.6072e-05)*phi*phi +   (0.0017069)*phi +  (-0.0027976))*pp +  ((6.8458e-05)*phi*phi +   (-0.004796)*phi +   (0.020065));
                }
            }
            
            // 5th Refinement Made on 8/14/2024
            if(sec == 1){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 1] is:
                dp = dp + ((-1.3461e-06)*phi*phi + (1.2220e-05)*phi + (4.0453e-04))*pp*pp + ((1.1275e-05)*phi*phi + (-7.2334e-05)*phi + (-0.0037741))*pp + ((-1.2556e-05)*phi*phi + (3.6897e-05)*phi + (0.0047898));
            }
            if(sec == 2){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 2] is:
                dp = dp + ((8.8958e-07)*phi*phi + (1.1594e-05)*phi + (-2.1837e-04))*pp*pp + ((-6.5454e-06)*phi*phi + (-4.0303e-05)*phi + (0.0015182))*pp + ((2.0679e-06)*phi*phi + (-9.0161e-05)*phi + (-1.5056e-04));
            }
            if(sec == 3){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 3] is:
                dp = dp + ((3.7278e-07)*phi*phi + (-1.0391e-05)*phi + (-7.7620e-05))*pp*pp + ((-5.3408e-06)*phi*phi + (1.0286e-04)*phi + (6.0048e-04))*pp + ((8.4599e-06)*phi*phi + (-1.9268e-04)*phi + (5.4090e-05));
            }
            if(sec == 4){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 4] is:
                dp = dp + ((1.0263e-06)*phi*phi + (4.5781e-06)*phi + (-1.3922e-04))*pp*pp + ((-6.6979e-06)*phi*phi + (-5.3840e-05)*phi + (8.4739e-04))*pp + ((4.3399e-06)*phi*phi + (7.9334e-05)*phi + (5.5832e-04));
            }
            if(sec == 5){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 5] is:
                dp = dp + ((-4.3369e-07)*phi*phi + (4.7403e-06)*phi + (5.7200e-05))*pp*pp + ((5.0509e-06)*phi*phi + (-9.4318e-05)*phi + (-0.0011244))*pp + ((-1.0369e-05)*phi*phi + (2.4561e-04)*phi + (0.0025475));
            }
            if(sec == 6){
                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmfaP2_ELPipMMfaP2][Sector 6] is:
                dp = dp + ((4.2948e-08)*phi*phi + (1.8318e-05)*phi + (-2.2139e-04))*pp*pp + ((-2.0052e-07)*phi*phi + (-1.2731e-04)*phi + (0.0015941))*pp + ((-5.6875e-06)*phi*phi + (1.9029e-04)*phi + (-5.6956e-04));
            }
            
        }

    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //====================================================================================================================================//
    //=======================//=======================//      π+ Corrections (End)      //=======================//=======================//
    //====================================================================================================================================//
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
    
    
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //====================================================================================================================================//
    //=========================//=========================//     π- Corrections     //=========================//=========================//
    //====================================================================================================================================//
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    if(ivec == 2 && corPim != 0){
        if(sec == 1){
            dp = ((2.7123584594392597e-06)*phi*phi + (-5.468601175954242e-05)*phi + (0.002313330256974031))*pp*pp + ((-8.039703360516874e-06)*phi*phi + (0.00044464879674067275)*phi + (-0.02546911446157775))*pp + ((3.5973669277966655e-06)*phi*phi + (-0.0003856844699023182)*phi + (0.05496480659602064) - 0.015);
        }
        if(sec == 2){
            dp = ((1.9081500905303347e-06)*phi*phi + (3.310647986349362e-05)*phi + (-0.0003264357817968204))*pp*pp + ((-1.2306311457915714e-05)*phi*phi + (-6.404982516446639e-05)*phi + (-0.01287404671840319))*pp + ((9.746651642120768e-06)*phi*phi + (6.1503461629194e-05)*phi + (0.04249861359511857) - 0.015);
        }
        if(sec == 3){
            dp = ((3.467960715633796e-06)*phi*phi + (-0.00011427345789836184)*phi + (0.004780571116355615))*pp*pp + ((-1.2639455891842017e-05)*phi*phi + (0.00044737258600913664)*phi + (-0.03827009444373719))*pp + ((5.8243648992776484e-06)*phi*phi + (-0.0004240381542174731)*phi + (0.06589846610477122) - 0.015);
        }
        if(sec == 4){
            dp = ((-7.97757466039691e-06)*phi*phi + (-0.00011075801628158914)*phi + (0.006505144041475733))*pp*pp + ((3.570788801587046e-05)*phi*phi + (0.0005835525352273808)*phi + (-0.045031773715754606))*pp + ((-3.223327114068019e-05)*phi*phi + (-0.0006144362450858762)*phi + (0.07280937684254037) - 0.015);
        }
        if(sec == 5){
            dp = ((1.990802625607816e-06)*phi*phi + (7.057771450607931e-05)*phi + (0.005399025205722829))*pp*pp + ((-7.670376562908147e-06)*phi*phi + (-0.00032508260930191955)*phi + (-0.044439500813069875))*pp + ((7.599354976329091e-06)*phi*phi + (0.0002562152836894338)*phi + (0.07195292224032898) - 0.015);
        }
        if(sec == 6){
            dp = ((1.9247834787602347e-06)*phi*phi + (7.638857332736951e-05)*phi + (0.005271258583881754))*pp*pp + ((-2.7349724034956845e-06)*phi*phi + (-0.00016130256163798413)*phi + (-0.03668300882287307))*pp + ((7.40942843287096e-07)*phi*phi + (-5.785254680184232e-05)*phi + (0.06282320712979896) - 0.015);
        }
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //====================================================================================================================================//
    //=======================//=======================//      π- Corrections (End)      //=======================//=======================//
    //====================================================================================================================================//
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //====================================================================================================================================//
    //========================//========================//     Proton Corrections     //========================//========================//
    //====================================================================================================================================//
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    if(ivec == 3 && corPro != 0){ // Quadratic Momentum - No Phi Dependence

        if(sec == 1){
            dp = (-4.30864e-03)*pp*pp + (1.53688e-02)*pp + (-1.66676e-02);                    
            // From GitHub_F_Pro for GitHub_F2_Pro:
            // The QUADRATIC function predicted for Δp_{pro} for [Outbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 1][All Pro Phi Bins] is:
            dp = dp + ((-4.3301e-04)*pp*pp + (1.4483e-03)*pp + (-1.1343e-03));
        }

        if(sec == 2){
            dp = (-1.29444e-02)*pp*pp + (4.11823e-02)*pp + (-3.4069e-02);                    
            // From GitHub_F_Pro for GitHub_F2_Pro:
            // The QUADRATIC function predicted for Δp_{pro} for [Outbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 2][All Pro Phi Bins] is:
            dp = dp + ((5.2462e-04)*pp*pp + (-1.4881e-03)*pp + (8.0050e-04));
        }

        if(sec == 3){
            dp = (-9.36605e-03)*pp*pp + (3.25537e-02)*pp + (-3.41826e-02);                    
            // From GitHub_F_Pro for GitHub_F2_Pro:
            // The QUADRATIC function predicted for Δp_{pro} for [Outbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 3][All Pro Phi Bins] is:
            dp = dp + ((-1.9155e-03)*pp*pp + (6.1540e-03)*pp + (-4.0436e-03));
        }

        if(sec == 4){
            dp = (-1.45314e-02)*pp*pp + (4.97218e-02)*pp + (-4.43198e-02);                    
            // From GitHub_F_Pro for GitHub_F2_Pro:
            // The QUADRATIC function predicted for Δp_{pro} for [Outbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 4][All Pro Phi Bins] is:
            dp = dp + ((5.9258e-04)*pp*pp + (-3.7177e-04)*pp + (-2.3707e-04));
        }

        if(sec == 5){
            dp = (-1.08441e-02)*pp*pp + (3.89079e-02)*pp + (-3.68669e-02);                    
            // From GitHub_F_Pro for GitHub_F2_Pro:
            // The QUADRATIC function predicted for Δp_{pro} for [Outbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 5][All Pro Phi Bins] is:
            dp = dp + ((-5.5398e-04)*pp*pp + (2.3721e-03)*pp + (-2.3279e-03));
        }

        if(sec == 6){
            dp = (-4.55633e-03)*pp*pp + (1.75565e-02)*pp + (-1.74574e-02);                    
            // From GitHub_F_Pro for GitHub_F2_Pro:
            // The QUADRATIC function predicted for Δp_{pro} for [Outbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 6][All Pro Phi Bins] is:
            dp = dp + ((-1.1516e-03)*pp*pp + (3.0094e-03)*pp + (-8.2480e-04));
        }

    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //====================================================================================================================================//
    //======================//=======================//     Proton Corrections (End)     //=======================//======================//
    //====================================================================================================================================//
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    return dp/pp;
};

"""])

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

###########################################################################
#----------#      Proton Energy Loss Corrections (Pass 1)      #----------#
###########################################################################
def Proton_Energy_Loss_Cor_Function(Bending_Type="In"):
    ELoss_Correction = ''.join(["""

    double dE_loss = 0;
    //=====// My Version of Andrey's Proton Energy Loss Correction //=====//
    """, """
    // Inbending Energy Loss Correction //
    if(proth < 27){
        dE_loss = exp(-2.739 - 3.932*pro); // + 0.002907;
    }
    if(proth > 27){
        dE_loss = exp(-1.2 - 4.228*pro); // + 0.007502;
    }
    """ if("In" in Bending_Type) else """
    // Outbending Energy Loss Correction //
    if(proth > 27){
        dE_loss = exp(-1.871 - 3.063*pro); // + 0.007517;
    }
    """, """
    double feloss = (pro + dE_loss)/pro;

    """])
    return ELoss_Correction



############################################################################
#----------#      π+ Pion Energy Loss Corrections (Pass 2)      #----------#
############################################################################
Pion_Energy_Loss_Cor_Function = """
auto eloss_pip = [&](double pion_p, double pip_theta, double pion_det, bool outbending){
    // momentum loss correction for low momentum pions:
    // input: p = pion momentum in GeV, pip_theta = pion theta in degree, 
    //        pion_det = pion detector (2 = FD, 3 = CD),  outbending = torus polarity
    // output: dp_pion = generated momentum - reconstructed momentum = momentum loss (+) / gain (-)

    double dp_pion = 0.0;

    if(outbending == false){ // INBENDING
        if(pion_det == 2){   // Forward Detector
            if(pip_theta < 27){                                       dp_pion =  0.00342646 + (-0.00282934) *pion_p + (0.00205983)   *pow(pion_p,2) + (-0.00043158)  *pow(pion_p,3) + (0) *pow(pion_p,4);}
            if(pip_theta < 27 && pion_p >= 2.5){                      dp_pion =  0.00342646 + (-0.00282934) *2.5    + (0.00205983)   *pow(2.5,2)    + (-0.00043158)  *pow(2.5,3)    + (0) *pow(2.5,4);}
            if(pip_theta > 27 && pip_theta < 28){                     dp_pion =  0.00328565 + (-0.00376042) *pion_p + (0.00433886)   *pow(pion_p,2) + (-0.00141614)  *pow(pion_p,3) + (0) *pow(pion_p,4);}
            if(pip_theta > 27 && pip_theta < 28 && pion_p >= 1.83){   dp_pion =  0.00328565 + (-0.00376042) *1.83   + (0.00433886)   *pow(1.83,2)   + (-0.00141614)  *pow(1.83,3)   + (0) *pow(1.83,4);}
            if(pip_theta > 28 && pip_theta < 29){                     dp_pion =  0.00328579 + (-0.00281121) *pion_p + (0.00342749)   *pow(pion_p,2) + (-0.000932614) *pow(pion_p,3) + (0) *pow(pion_p,4);}
            if(pip_theta > 28 && pip_theta < 29 && pion_p >= 2){      dp_pion =  0.00328579 + (-0.00281121) *2      + (0.00342749)   *pow(2,2)      + (-0.000932614) *pow(2,3)      + (0) *pow(2,4);}
            if(pip_theta > 29 && pip_theta < 30){                     dp_pion =  0.00167358 + (0.00441871)  *pion_p + (-0.000834667) *pow(pion_p,2) + (-0.000137968) *pow(pion_p,3) + (0) *pow(pion_p,4);}
            if(pip_theta > 29 && pip_theta < 30 && pion_p >= 1.9){    dp_pion =  0.00167358 + (0.00441871)  *1.9    + (-0.000834667) *pow(1.9,2)    + (-0.000137968) *pow(1.9,3)    + (0) *pow(1.9,4);}
            if(pip_theta > 30 && pip_theta < 31){                     dp_pion =  0.00274159 + (0.00635686)  *pion_p + (-0.00380977)  *pow(pion_p,2) + (0.00071627)   *pow(pion_p,3) + (0) *pow(pion_p,4);}
            if(pip_theta > 30 && pip_theta < 31 && pion_p >= 1.9){    dp_pion =  0.00274159 + (0.00635686)  *1.9    + (-0.00380977)  *pow(1.9,2)    + (0.00071627)   *pow(1.9,3)    + (0) *pow(1.9,4);}
            if(pip_theta > 31 && pip_theta < 32){                     dp_pion =  0.00450241 + (0.00248969)  *pion_p + (-0.00336795)  *pow(pion_p,2) + (0.00111193)   *pow(pion_p,3) + (0) *pow(pion_p,4);}
            if(pip_theta > 31 && pip_theta < 32 && pion_p >= 1.8){    dp_pion =  0.00450241 + (0.00248969)  *1.8    + (-0.00336795)  *pow(1.8,2)    + (0.00111193)   *pow(1.8,3)    + (0) *pow(1.8,4);}
            if(pip_theta > 32 && pip_theta < 33){                     dp_pion =  0.00505593 + (-0.00246203) *pion_p + (0.00172984)   *pow(pion_p,2) + (-0.000406701) *pow(pion_p,3) + (0) *pow(pion_p,4);}
            if(pip_theta > 32 && pip_theta < 33 && pion_p >= 1.8){    dp_pion =  0.00505593 + (-0.00246203) *1.8    + (0.00172984)   *pow(1.8,2)    + (-0.000406701) *pow(1.8,3)    + (0) *pow(1.8,4);}
            if(pip_theta > 33 && pip_theta < 34){                     dp_pion =  0.00273402 + (0.00440449)  *pion_p + (-0.00373488)  *pow(pion_p,2) + (0.000996612)  *pow(pion_p,3) + (0) *pow(pion_p,4);}
            if(pip_theta > 33 && pip_theta < 34 && pion_p >= 1.8){    dp_pion =  0.00273402 + (0.00440449)  *1.8    + (-0.00373488)  *pow(1.8,2)    + (0.000996612)  *pow(1.8,3)    + (0) *pow(1.8,4);}
            if(pip_theta > 34 && pip_theta < 35){                     dp_pion =  0.00333542 + (0.00439874)  *pion_p + (-0.00397776)  *pow(pion_p,2) + (0.00105586)   *pow(pion_p,3) + (0) *pow(pion_p,4);}
            if(pip_theta > 34 && pip_theta < 35 && pion_p >= 1.8){    dp_pion =  0.00333542 + (0.00439874)  *1.8    + (-0.00397776)  *pow(1.8,2)    + (0.00105586)   *pow(1.8,3)    + (0) *pow(1.8,4);}
            if(pip_theta > 35 && pip_theta < 36){                     dp_pion =  0.00354663 + (0.00565397)  *pion_p + (-0.00513503)  *pow(pion_p,2) + (0.00153346)   *pow(pion_p,3) + (0) *pow(pion_p,4);}
            if(pip_theta > 35 && pip_theta < 36 && pion_p >= 1.8){    dp_pion =  0.00354663 + (0.00565397)  *1.8    + (-0.00513503)  *pow(1.8,2)    + (0.00153346)   *pow(1.8,3)    + (0) *pow(1.8,4);}
            if(pip_theta > 36 && pip_theta < 37){                     dp_pion =  0.00333909 + (0.00842367)  *pion_p + (-0.0077321)   *pow(pion_p,2) + (0.0022489)    *pow(pion_p,3) + (0) *pow(pion_p,4);}
            if(pip_theta > 36 && pip_theta < 37 && pion_p >= 1.8){    dp_pion =  0.00333909 + (0.00842367)  *1.8    + (-0.0077321)   *pow(1.8,2)    + (0.0022489)    *pow(1.8,3)    + (0) *pow(1.8,4);}
            if(pip_theta > 37 && pip_theta < 38){                     dp_pion =  0.00358828 + (0.0112108)   *pion_p + (-0.0133854)   *pow(pion_p,2) + (0.00486924)   *pow(pion_p,3) + (0) *pow(pion_p,4);}
            if(pip_theta > 37 && pip_theta < 38 && pion_p >= 1.4){    dp_pion =  0.00358828 + (0.0112108)   *1.4    + (-0.0133854)   *pow(1.4,2)    + (0.00486924)   *pow(1.4,3)    + (0) *pow(1.4,4);}
            if(pip_theta > 38 && pip_theta < 39){                     dp_pion =  0.00354343 + (0.0117121)   *pion_p + (-0.0129649)   *pow(pion_p,2) + (0.00455602)   *pow(pion_p,3) + (0) *pow(pion_p,4);}
            if(pip_theta > 38 && pip_theta < 39 && pion_p >= 1.3){    dp_pion =  0.00354343 + (0.0117121)   *1.3    + (-0.0129649)   *pow(1.3,2)    + (0.00455602)   *pow(1.3,3)    + (0) *pow(1.3,4);}
            if(pip_theta > 39 && pip_theta < 40){                     dp_pion = -0.00194951 + (0.0409713)   *pion_p + (-0.0595861)   *pow(pion_p,2) + (0.0281588)    *pow(pion_p,3) + (0) *pow(pion_p,4);}
            if(pip_theta > 39 && pip_theta < 40 && pion_p >= 0.9){    dp_pion = -0.00194951 + (0.0409713)   *0.9    + (-0.0595861)   *pow(0.9,2)    + (0.0281588)    *pow(0.9,3)    + (0) *pow(0.9,4);}
            if(pip_theta > 40 && pip_theta < 41){                     dp_pion = -0.0099217  + (0.0808096)   *pion_p + (-0.119836)    *pow(pion_p,2) + (0.0559553)    *pow(pion_p,3) + (0) *pow(pion_p,4);}
            if(pip_theta > 40 && pip_theta < 41 && pion_p >= 0.75){   dp_pion = -0.0099217  + (0.0808096)   *0.75   + (-0.119836)    *pow(0.75,2)   + (0.0559553)    *pow(0.75,3)   + (0) *pow(0.75,4);}
            if(pip_theta > 41 && pip_theta < 42){                     dp_pion =  0.00854898 + (0.00025037)  *pion_p + (-0.0113992)   *pow(pion_p,2) + (0.0145178)    *pow(pion_p,3) + (0) *pow(pion_p,4);}
            if(pip_theta > 41 && pip_theta < 42 && pion_p >= 0.65){   dp_pion =  0.00854898 + (0.00025037)  *0.65   + (-0.0113992)   *pow(0.65,2)   + (0.0145178)    *pow(0.65,3)   + (0) *pow(0.65,4);}
            if(pip_theta > 42){                                       dp_pion =  0.00564818 + (0.00706606)  *pion_p + (0.0042602)    *pow(pion_p,2) + (-0.01141)     *pow(pion_p,3) + (0) *pow(pion_p,4);}
            if(pip_theta > 42 && pion_p >= 0.65){                     dp_pion =  0.00564818 + (0.00706606)  *0.65   + (0.0042602)    *pow(0.65,2)   + (-0.01141)     *pow(0.65,3)   + (0) *pow(0.65,4);}
        }
        if(pion_det == 3){  // Central Detector
            if(pip_theta < 39){                                       dp_pion = -0.045      + (-0.102652) + (0.455589) *pion_p + (-0.671635)   *pow(pion_p,2) + (0.303814)   *pow(pion_p,3);}
            if(pip_theta < 39  && pion_p >= 0.7){                     dp_pion = -0.045      + (-0.102652) + (0.455589) *0.7    + (-0.671635)   *pow(0.7,2)    + (0.303814)   *pow(0.7,3);}
            if(pip_theta > 39  && pip_theta < 40){                    dp_pion =  0.0684552  + (-0.766492)              *pion_p + (1.73092)     *pow(pion_p,2) + (-1.46215)   *pow(pion_p,3) + (0.420127) *pow(pion_p,4);}
            if(pip_theta > 39  && pip_theta < 40 && pion_p >= 1.4){   dp_pion =  0.0684552  + (-0.766492)              *1.4    + (1.73092)     *pow(1.4,2)    + (-1.46215)   *pow(1.4,3)    + (0.420127) *pow(1.4,4);}
            if(pip_theta > 40  && pip_theta < 41){                    dp_pion =  0.751549   + (-7.4593)                *pion_p + (26.8037)     *pow(pion_p,2) + (-47.1576)   *pow(pion_p,3) + (43.8527)  *pow(pion_p,4) + (-20.7039) *pow(pion_p,5) + (3.90931)  *pow(pion_p,6);}
            if(pip_theta > 40  && pip_theta < 41 && pion_p >= 1.45){  dp_pion =  0.751549   + (-7.4593)                *1.45   + (26.8037)     *pow(1.45,2)   + (-47.1576)   *pow(1.45,3)   + (43.8527)  *pow(1.45,4)   + (-20.7039) *pow(1.45,5)   + (3.90931)  *pow(1.45,6);}
            if(pip_theta > 41  && pip_theta < 42){                    dp_pion = -1.35043    + (10.0788)                *pion_p + (-30.4829)    *pow(pion_p,2) + (47.7792)    *pow(pion_p,3) + (-40.996)  *pow(pion_p,4) + (18.2662)  *pow(pion_p,5) + (-3.30449) *pow(pion_p,6);}
            if(pip_theta > 41  && pip_theta < 42 && pion_p >= 1.2){   dp_pion = -1.35043    + (10.0788)                *1.2    + (-30.4829)    *pow(1.2,2)    + (47.7792)    *pow(1.2,3)    + (-40.996)  *pow(1.2,4)    + (18.2662)  *pow(1.2,5)    + (-3.30449) *pow(1.2,6);}
            if(pip_theta > 42  && pip_theta < 43){                    dp_pion = -0.0231195  + (0.0744589)              *pion_p + (-0.0807029)  *pow(pion_p,2) + (0.0264266)  *pow(pion_p,3) + (0)        *pow(pion_p,4);}
            if(pip_theta > 42  && pip_theta < 43 && pion_p >= 1.3){   dp_pion = -0.0231195  + (0.0744589)              *1.3    + (-0.0807029)  *pow(1.3,2)    + (0.0264266)  *pow(1.3,3)    + (0)        *pow(1.3,4);}
            if(pip_theta > 43  && pip_theta < 44){                    dp_pion = -0.00979928 + (0.0351043)              *pion_p + (-0.0365865)  *pow(pion_p,2) + (0.00977218) *pow(pion_p,3) + (0)        *pow(pion_p,4);}
            if(pip_theta > 43  && pip_theta < 44 && pion_p >= 1.1){   dp_pion = -0.00979928 + (0.0351043)              *1.1    + (-0.0365865)  *pow(1.1,2)    + (0.00977218) *pow(1.1,3)    + (0)        *pow(1.1,4);}
            if(pip_theta > 44  && pip_theta < 45){                    dp_pion =  0.00108491 + (-0.00924885)            *pion_p + (0.0216431)   *pow(pion_p,2) + (-0.0137762) *pow(pion_p,3) + (0)        *pow(pion_p,4);}
            if(pip_theta > 44  && pip_theta < 45 && pion_p >= 1.1){   dp_pion =  0.00108491 + (-0.00924885)            *1.1    + (0.0216431)   *pow(1.1,2)    + (-0.0137762) *pow(1.1,3)    + (0)        *pow(1.1,4);}
            if(pip_theta > 45  && pip_theta < 55){                    dp_pion =  0.0092263  + (-0.0676178)             *pion_p + (0.168778)    *pow(pion_p,2) + (-0.167463)  *pow(pion_p,3) + (0.05661)  *pow(pion_p,4);}
            if(pip_theta > 45  && pip_theta < 55 && pion_p >= 1.3){   dp_pion =  0.0092263  + (-0.0676178)             *1.3    + (0.168778)    *pow(1.3,2)    + (-0.167463)  *pow(1.3,3)    + (0.05661)  *pow(1.3,4);}
            if(pip_theta > 55  && pip_theta < 65){                    dp_pion =  0.00805642 + (-0.0670962)             *pion_p + (0.188536)    *pow(pion_p,2) + (-0.20571)   *pow(pion_p,3) + (0.0765)   *pow(pion_p,4);}
            if(pip_theta > 55  && pip_theta < 65 && pion_p >= 1.05){  dp_pion =  0.00805642 + (-0.0670962)             *1.05   + (0.188536)    *pow(1.05,2)   + (-0.20571)   *pow(1.05,3)   + (0.0765)   *pow(1.05,4);}
            if(pip_theta > 65  && pip_theta < 75){                    dp_pion =  0.00312202 + (-0.0269717)             *pion_p + (0.0715236)   *pow(pion_p,2) + (-0.0545622) *pow(pion_p,3) + (0)        *pow(pion_p,4);}
            if(pip_theta > 65  && pip_theta < 75 && pion_p >= 0.75){  dp_pion =  0.00312202 + (-0.0269717)             *0.75   + (0.0715236)   *pow(0.75,2)   + (-0.0545622) *pow(0.75,3)   + (0)        *pow(0.75,4);}
            if(pip_theta > 75  && pip_theta < 85){                    dp_pion =  0.00424971 + (-0.0367683)             *pion_p + (0.10417)     *pow(pion_p,2) + (-0.0899651) *pow(pion_p,3) + (0)        *pow(pion_p,4);}
            if(pip_theta > 75  && pip_theta < 85 && pion_p >= 0.65){  dp_pion =  0.00424971 + (-0.0367683)             *0.65   + (0.10417)     *pow(0.65,2)   + (-0.0899651) *pow(0.65,3)   + (0)        *pow(0.65,4);}
            if(pip_theta > 85  && pip_theta < 95){                    dp_pion =  0.00654123 + (-0.0517915)             *pion_p + (0.147888)    *pow(pion_p,2) + (-0.14253)   *pow(pion_p,3) + (0)        *pow(pion_p,4);}
            if(pip_theta > 85  && pip_theta < 95 && pion_p >= 0.5){   dp_pion =  0.00654123 + (-0.0517915)             *0.5    + (0.147888)    *pow(0.5,2)    + (-0.14253)   *pow(0.5,3)    + (0)        *pow(0.5,4);}
            if(pip_theta > 95  && pip_theta < 105){                   dp_pion = -0.00111721 + (0.00478119)             *pion_p + (0.0158753)   *pow(pion_p,2) + (-0.052902)  *pow(pion_p,3) + (0)        *pow(pion_p,4);}
            if(pip_theta > 95  && pip_theta < 105 && pion_p >= 0.45){ dp_pion = -0.00111721 + (0.00478119)             *0.45   + (0.0158753)   *pow(0.45,2)   + (-0.052902)  *pow(0.45,3)   + (0)        *pow(0.45,4);}
            if(pip_theta > 105 && pip_theta < 115){                   dp_pion = -0.00239839 + (0.00790738)             *pion_p + (0.0311713)   *pow(pion_p,2) + (-0.104157)  *pow(pion_p,3) + (0)        *pow(pion_p,4);}
            if(pip_theta > 105 && pip_theta < 115 && pion_p >= 0.35){ dp_pion = -0.00239839 + (0.00790738)             *0.35   + (0.0311713)   *pow(0.35,2)   + (-0.104157)  *pow(0.35,3)   + (0)        *pow(0.35,4);}
            if(pip_theta > 115 && pip_theta < 125){                   dp_pion = -0.00778793 + (0.0256774)              *pion_p + (0.0932503)   *pow(pion_p,2) + (-0.32771)   *pow(pion_p,3) + (0)        *pow(pion_p,4);}
            if(pip_theta > 115 && pip_theta < 125 && pion_p >= 0.35){ dp_pion = -0.00778793 + (0.0256774)              *0.35   + (0.0932503)   *pow(0.35,2)   + (-0.32771)   *pow(0.35,3)   + (0)        *pow(0.35,4);}
            if(pip_theta > 125 && pip_theta < 135){                   dp_pion = -0.00292778 + (-0.00536697)            *pion_p + (-0.00414351) *pow(pion_p,2) + (0.0196431)  *pow(pion_p,3) + (0)        *pow(pion_p,4);}
            if(pip_theta > 125 && pip_theta < 135 && pion_p >= 0.35){ dp_pion = -0.00292778 + (-0.00536697)            *0.35   + (-0.00414351) *pow(0.35,2)   + (0.0196431)  *pow(0.35,3)   + (0)        *pow(0.35,4);}
        }
    }
    if(outbending == true){ // OUTBENDING
        if(pion_det == 2){  // Forward Detector
            if(pip_theta < 27){                                       dp_pion = 0.00389945  + (-0.004062)    *pion_p + (0.00321842)  *pow(pion_p,2) + (-0.000698299) *pow(pion_p,3) + (0)          *pow(pion_p,4);}
            if(pip_theta < 27 && pion_p >= 2.3){                      dp_pion = 0.00389945  + (-0.004062)    *2.3    + (0.00321842)  *pow(2.3,2)    + (-0.000698299) *pow(2.3,3)    + (0)          *pow(2.3,4);}
            if(pip_theta > 27 && pip_theta < 28){                     dp_pion = 0.00727132  + (-0.0117989)   *pion_p + (0.00962999)  *pow(pion_p,2) + (-0.00267005)  *pow(pion_p,3) + (0)          *pow(pion_p,4);}
            if(pip_theta > 27 && pip_theta < 28 && pion_p >= 1.7){    dp_pion = 0.00727132  + (-0.0117989)   *1.7    + (0.00962999)  *pow(1.7,2)    + (-0.00267005)  *pow(1.7,3)    + (0)          *pow(1.7,4);}
            if(pip_theta > 28 && pip_theta < 29){                     dp_pion = 0.00844551  + (-0.0128097)   *pion_p + (0.00945956)  *pow(pion_p,2) + (-0.00237992)  *pow(pion_p,3) + (0)          *pow(pion_p,4);}
            if(pip_theta > 28 && pip_theta < 29 && pion_p >= 2){      dp_pion = 0.00844551  + (-0.0128097)   *2      + (0.00945956)  *pow(2,2)      + (-0.00237992)  *pow(2,3)      + (0)          *pow(2,4);}
            if(pip_theta > 29 && pip_theta < 30){                     dp_pion = 0.00959007  + (-0.0139218)   *pion_p + (0.0122966)   *pow(pion_p,2) + (-0.0034012)   *pow(pion_p,3) + (0)          *pow(pion_p,4);}
            if(pip_theta > 29 && pip_theta < 30 && pion_p >= 1.9){    dp_pion = 0.00959007  + (-0.0139218)   *1.9    + (0.0122966)   *pow(1.9,2)    + (-0.0034012)   *pow(1.9,3)    + (0)          *pow(1.9,4);}
            if(pip_theta > 30 && pip_theta < 31){                     dp_pion = 0.00542816  + (-5.10739e-05) *pion_p + (0.000572038) *pow(pion_p,2) + (-0.000488883) *pow(pion_p,3) + (0)          *pow(pion_p,4);}
            if(pip_theta > 30 && pip_theta < 31 && pion_p >= 1.9){    dp_pion = 0.00542816  + (-5.10739e-05) *1.9    + (0.000572038) *pow(1.9,2)    + (-0.000488883) *pow(1.9,3)    + (0)          *pow(1.9,4);}
            if(pip_theta > 31 && pip_theta < 32){                     dp_pion = 0.0060391   + (-0.000516936) *pion_p + (-0.00286595) *pow(pion_p,2) + (0.00136604)   *pow(pion_p,3) + (0)          *pow(pion_p,4);}
            if(pip_theta > 31 && pip_theta < 32 && pion_p >= 1.8){    dp_pion = 0.0060391   + (-0.000516936) *1.8    + (-0.00286595) *pow(1.8,2)    + (0.00136604)   *pow(1.8,3)    + (0)          *pow(1.8,4);}
            if(pip_theta > 32 && pip_theta < 33){                     dp_pion = 0.0140305   + (-0.0285832)   *pion_p + (0.0248799)   *pow(pion_p,2) + (-0.00701311)  *pow(pion_p,3) + (0)          *pow(pion_p,4);}
            if(pip_theta > 32 && pip_theta < 33 && pion_p >= 1.6){    dp_pion = 0.0140305   + (-0.0285832)   *1.6    + (0.0248799)   *pow(1.6,2)    + (-0.00701311)  *pow(1.6,3)    + (0)          *pow(1.6,4);}
            if(pip_theta > 33 && pip_theta < 34){                     dp_pion = 0.010815    + (-0.0194244)   *pion_p + (0.0174474)   *pow(pion_p,2) + (-0.0049764)   *pow(pion_p,3) + (0)          *pow(pion_p,4);}
            if(pip_theta > 33 && pip_theta < 34 && pion_p >= 1.5){    dp_pion = 0.010815    + (-0.0194244)   *1.5    + (0.0174474)   *pow(1.5,2)    + (-0.0049764)   *pow(1.5,3)    + (0)          *pow(1.5,4);}
            if(pip_theta > 34 && pip_theta < 35){                     dp_pion = 0.0105522   + (-0.0176248)   *pion_p + (0.0161142)   *pow(pion_p,2) + (-0.00472288)  *pow(pion_p,3) + (0)          *pow(pion_p,4);}
            if(pip_theta > 34 && pip_theta < 35 && pion_p >= 1.6){    dp_pion = 0.0105522   + (-0.0176248)   *1.6    + (0.0161142)   *pow(1.6,2)    + (-0.00472288)  *pow(1.6,3)    + (0)          *pow(1.6,4);}
            if(pip_theta > 35 && pip_theta < 36){                     dp_pion = 0.0103938   + (-0.0164003)   *pion_p + (0.0164045)   *pow(pion_p,2) + (-0.00517012)  *pow(pion_p,3) + (0)          *pow(pion_p,4);}
            if(pip_theta > 35 && pip_theta < 36 && pion_p >= 1.5){    dp_pion = 0.0103938   + (-0.0164003)   *1.5    + (0.0164045)   *pow(1.5,2)    + (-0.00517012)  *pow(1.5,3)    + (0)          *pow(1.5,4);}
            if(pip_theta > 36 && pip_theta < 37){                     dp_pion = 0.0441471   + (-0.183937)    *pion_p + (0.338784)    *pow(pion_p,2) + (-0.298985)    *pow(pion_p,3) + (0.126905)   *pow(pion_p,4) + (-0.0208286) *pow(pion_p,5);}
            if(pip_theta > 36 && pip_theta < 37 && pion_p >= 1.8){    dp_pion = 0.0441471   + (-0.183937)    *1.8    + (0.338784)    *pow(1.8,2)    + (-0.298985)    *pow(1.8,3)    + (0.126905)   *pow(1.8,4)    + (-0.0208286) *pow(1.8,5);}
            if(pip_theta > 37 && pip_theta < 38){                     dp_pion = 0.0726119   + (-0.345004)    *pion_p + (0.697789)    *pow(pion_p,2) + (-0.685948)    *pow(pion_p,3) + (0.327195)   *pow(pion_p,4) + (-0.0605621) *pow(pion_p,5);}
            if(pip_theta > 37 && pip_theta < 38 && pion_p >= 1.7){    dp_pion = 0.0726119   + (-0.345004)    *1.7    + (0.697789)    *pow(1.7,2)    + (-0.685948)    *pow(1.7,3)    + (0.327195)   *pow(1.7,4)    + (-0.0605621) *pow(1.7,5);}
            if(pip_theta > 38 && pip_theta < 39){                     dp_pion = 0.0247648   + (-0.0797376)   *pion_p + (0.126535)    *pow(pion_p,2) + (-0.086545)    *pow(pion_p,3) + (0.0219304)  *pow(pion_p,4);}
            if(pip_theta > 38 && pip_theta < 39 && pion_p >= 1.6){    dp_pion = 0.0247648   + (-0.0797376)   *1.6    + (0.126535)    *pow(1.6,2)    + (-0.086545)    *pow(1.6,3)    + (0.0219304)  *pow(1.6,4);}
            if(pip_theta > 39 && pip_theta < 40){                     dp_pion = 0.0208867   + (-0.0492068)   *pion_p + (0.0543187)   *pow(pion_p,2) + (-0.0183393)   *pow(pion_p,3) + (0)          *pow(pion_p,4);}
            if(pip_theta > 39 && pip_theta < 40 && pion_p >= 1.2){    dp_pion = 0.0208867   + (-0.0492068)   *1.2    + (0.0543187)   *pow(1.2,2)    + (-0.0183393)   *pow(1.2,3)    + (0)          *pow(1.2,4);}
            if(pip_theta > 40 && pip_theta < 41){                     dp_pion = 0.0148655   + (-0.0203483)   *pion_p + (0.00835867)  *pow(pion_p,2) + (0.00697134)   *pow(pion_p,3) + (0)          *pow(pion_p,4);}
            if(pip_theta > 40 && pip_theta < 41 && pion_p >= 1.0){    dp_pion = 0.0148655   + (-0.0203483)   *1.0    + (0.00835867)  *pow(1.0,2)    + (0.00697134)   *pow(1.0,3)    + (0)          *pow(1.0,4);}
            if(pip_theta > 41 && pip_theta < 42){                     dp_pion = 0.0223585   + (-0.0365262)   *pion_p + (-0.0150027)  *pow(pion_p,2) + (0.0854164)    *pow(pion_p,3) + (-0.0462718) *pow(pion_p,4);}
            if(pip_theta > 41 && pip_theta < 42 && pion_p >= 0.7){    dp_pion = 0.007617;}
            if(pip_theta > 42){                                       dp_pion = 0.0152373   + (-0.0106377)   *pion_p + (-0.0257573)  *pow(pion_p,2) + (0.0344851)    *pow(pion_p,3) + (0)          *pow(pion_p,4);}
            if(pip_theta > 42 && pion_p >= 0.75){                     dp_pion = 0.0152373   + (-0.0106377)   *0.75   + (-0.0257573)  *pow(0.75,2)   + (0.0344851)    *pow(0.75,3)   + (0)          *pow(0.75,4);}
        }
        if(pion_det == 3){ // Central Detector
            if(pip_theta < 39){                                       dp_pion = -0.05        + (-0.0758897) + (0.362231) *pion_p + (-0.542404)   *pow(pion_p,2) + (0.241344)   *pow(pion_p,3);}
            if(pip_theta < 39  && pion_p >= 0.8){                     dp_pion = -0.05        + (-0.0758897) + (0.362231) *0.8    + (-0.542404)   *pow(0.8,2)    + (0.241344)   *pow(0.8,3);}
            if(pip_theta > 39  && pip_theta < 40){                    dp_pion =  0.0355259   + (-0.589712)               *pion_p + (1.4206)      *pow(pion_p,2) + (-1.24179)   *pow(pion_p,3) + (0.365524)  *pow(pion_p,4);}
            if(pip_theta > 39  && pip_theta < 40  && pion_p >= 1.35){ dp_pion =  0.0355259   + (-0.589712)               *1.35   + (1.4206)      *pow(1.35,2)   + (-1.24179)   *pow(1.35,3)   + (0.365524)  *pow(1.35,4);}
            if(pip_theta > 40  && pip_theta < 41){                    dp_pion = -0.252336    + (1.02032)                 *pion_p + (-1.51461)    *pow(pion_p,2) + (0.967772)   *pow(pion_p,3) + (-0.226028) *pow(pion_p,4);}
            if(pip_theta > 40  && pip_theta < 41  && pion_p >= 1.4){  dp_pion = -0.252336    + (1.02032)                 *1.4    + (-1.51461)    *pow(1.4,2)    + (0.967772)   *pow(1.4,3)    + (-0.226028) *pow(1.4,4);}
            if(pip_theta > 41  && pip_theta < 42){                    dp_pion = -0.710129    + (4.49613)                 *pion_p + (-11.01)      *pow(pion_p,2) + (12.9945)    *pow(pion_p,3) + (-7.41641)  *pow(pion_p,4) + (1.63923)   *pow(pion_p,5);}
            if(pip_theta > 41  && pip_theta < 42  && pion_p >= 1.2){  dp_pion = -0.710129    + (4.49613)                 *1.2    + (-11.01)      *pow(1.2,2)    + (12.9945)    *pow(1.2,3)    + (-7.41641)  *pow(1.2,4)    + (1.63923)   *pow(1.2,5);}
            if(pip_theta > 42  && pip_theta < 43){                    dp_pion = -0.0254912   + (0.0851432)               *pion_p + (-0.0968583)  *pow(pion_p,2) + (0.0350334)  *pow(pion_p,3) + (0)         *pow(pion_p,4);}
            if(pip_theta > 42  && pip_theta < 43  && pion_p >= 1.2){  dp_pion = -0.0254912   + (0.0851432)               *1.2    + (-0.0968583)  *pow(1.2,2)    + (0.0350334)  *pow(1.2,3)    + (0)         *pow(1.2,4);}
            if(pip_theta > 43  && pip_theta < 44){                    dp_pion = -0.0115965   + (0.0438726)               *pion_p + (-0.0500474)  *pow(pion_p,2) + (0.0163627)  *pow(pion_p,3) + (0)         *pow(pion_p,4);}
            if(pip_theta > 43  && pip_theta < 44  && pion_p >= 1.4){  dp_pion = -0.0115965   + (0.0438726)               *1.4    + (-0.0500474)  *pow(1.4,2)    + (0.0163627)  *pow(1.4,3)    + (0)         *pow(1.4,4);}
            if(pip_theta > 44  && pip_theta < 45){                    dp_pion =  0.00273414  + (-0.01851)                *pion_p + (0.0377032)   *pow(pion_p,2) + (-0.0226696) *pow(pion_p,3) + (0)         *pow(pion_p,4);}
            if(pip_theta > 44  && pip_theta < 45  && pion_p >= 1){    dp_pion =  0.00273414  + (-0.01851)                *1      + (0.0377032)   *pow(1,2)      + (-0.0226696) *pow(1,3)      + (0)         *pow(1,4);}
            if(pip_theta > 45  && pip_theta < 55){                    dp_pion =  0.0271952   + (-0.25981)                *pion_p + (0.960051)    *pow(pion_p,2) + (-1.76651)   *pow(pion_p,3) + (1.72872)   *pow(pion_p,4) + (-0.856946) *pow(pion_p,5) + (0.167564) *pow(pion_p,6);}
            if(pip_theta > 45  && pip_theta < 55  && pion_p >= 1.4){  dp_pion =  0.0271952   + (-0.25981)                *1.4    + (0.960051)    *pow(1.4,2)    + (-1.76651)   *pow(1.4,3)    + (1.72872)   *pow(1.4,4)    + (-0.856946) *pow(1.4,5)    + (0.167564) *pow(1.4,6);}
            if(pip_theta > 55  && pip_theta < 65){                    dp_pion =  0.00734975  + (-0.0598841)              *pion_p + (0.161495)    *pow(pion_p,2) + (-0.1629)    *pow(pion_p,3) + (0.0530098) *pow(pion_p,4);}
            if(pip_theta > 55  && pip_theta < 65  && pion_p >= 1.2){  dp_pion =  0.00734975  + (-0.0598841)              *1.2    + (0.161495)    *pow(1.2,2)    + (-0.1629)    *pow(1.2,3)    + (0.0530098) *pow(1.2,4);}
            if(pip_theta > 65  && pip_theta < 75){                    dp_pion =  0.00321351  + (-0.0289322)              *pion_p + (0.0786484)   *pow(pion_p,2) + (-0.0607041) *pow(pion_p,3) + (0)         *pow(pion_p,4);}
            if(pip_theta > 65  && pip_theta < 75  && pion_p >= 0.95){ dp_pion =  0.00321351  + (-0.0289322)              *0.95   + (0.0786484)   *pow(0.95,2)   + (-0.0607041) *pow(0.95,3)   + (0)         *pow(0.95,4);}
            if(pip_theta > 75  && pip_theta < 85){                    dp_pion =  0.00644253  + (-0.0543896)              *pion_p + (0.148933)    *pow(pion_p,2) + (-0.1256)    *pow(pion_p,3) + (0)         *pow(pion_p,4);}
            if(pip_theta > 75  && pip_theta < 85  && pion_p >= 0.7){  dp_pion =  0.00644253  + (-0.0543896)              *0.7    + (0.148933)    *pow(0.7,2)    + (-0.1256)    *pow(0.7,3)    + (0)         *pow(0.7,4);}
            if(pip_theta > 85  && pip_theta < 95){                    dp_pion =  0.00671152  + (-0.0537269)              *pion_p + (0.154509)    *pow(pion_p,2) + (-0.147667)  *pow(pion_p,3) + (0)         *pow(pion_p,4);}
            if(pip_theta > 85  && pip_theta < 95  && pion_p >= 0.65){ dp_pion =  0.00671152  + (-0.0537269)              *0.65   + (0.154509)    *pow(0.65,2)   + (-0.147667)  *pow(0.65,3)   + (0)         *pow(0.65,4);}
            if(pip_theta > 95  && pip_theta < 105){                   dp_pion = -0.000709077 + (0.00331818)              *pion_p + (0.0109241)   *pow(pion_p,2) + (-0.0351682) *pow(pion_p,3) + (0)         *pow(pion_p,4);}
            if(pip_theta > 95  && pip_theta < 105 && pion_p >= 0.45){ dp_pion = -0.000709077 + (0.00331818)              *0.45   + (0.0109241)   *pow(0.45,2)   + (-0.0351682) *pow(0.45,3)   + (0)         *pow(0.45,4);}
            if(pip_theta > 105 && pip_theta < 115){                   dp_pion = -0.00260164  + (0.00846919)              *pion_p + (0.0315497)   *pow(pion_p,2) + (-0.105756)  *pow(pion_p,3) + (0)         *pow(pion_p,4);}
            if(pip_theta > 105 && pip_theta < 115 && pion_p >= 0.45){ dp_pion = -0.00260164  + (0.00846919)              *0.45   + (0.0315497)   *pow(0.45,2)   + (-0.105756)  *pow(0.45,3)   + (0)         *pow(0.45,4);}
            if(pip_theta > 115 && pip_theta < 125){                   dp_pion = -0.00544336  + (0.018256)                *pion_p + (0.0664618)   *pow(pion_p,2) + (-0.240312)  *pow(pion_p,3) + (0)         *pow(pion_p,4);}
            if(pip_theta > 115 && pip_theta < 125 && pion_p >= 0.45){ dp_pion = -0.00544336  + (0.018256)                *0.45   + (0.0664618)   *pow(0.45,2)   + (-0.240312)  *pow(0.45,3)   + (0)         *pow(0.45,4);}
            if(pip_theta > 125 && pip_theta < 135){                   dp_pion = -0.00281073  + (-0.00495863)             *pion_p + (-0.00362356) *pow(pion_p,2) + (0.0178764)  *pow(pion_p,3) + (0)         *pow(pion_p,4);}
            if(pip_theta > 125 && pip_theta < 135 && pion_p >= 0.35){ dp_pion = -0.00281073  + (-0.00495863)             *0.35   + (-0.00362356) *pow(0.35,2)   + (0.0178764)  *pow(0.35,3)   + (0)         *pow(0.35,4);}
        }
    }

    return dp_pion;
};"""