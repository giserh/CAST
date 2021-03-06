stars_dialogs = '''
<?xml version="1.0" encoding="utf-8"?>
<resource>
  <object class="wxDialog" name="IDD_ABOUTBOX" subclass="CAboutDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>About OpenGeoDa</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTRE|wxALL</flag>
        <border>5</border>
        <object class="wxStaticBitmap" name="wxID_STATIC">
          <bitmap stock_id="about-geoda-logo"/>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTRE|wxALL|wxADJUST_MINSIZE</flag>
        <border>5</border>
        <object class="wxStaticText" name="IDC_STATIC">
          <label>Copyright (C) 1998-2011
GeoDa Center for Geospatial Analysis and Computation
and Arizona Board of Regents
All Rights Reserved</label>
          <style>wxALIGN_CENTRE</style>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_LEFT|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxHORIZONTAL</orient>
          <object class="sizeritem">
            <object class="wxStaticText" name="ID_STATICTEXT">
              <label>OpenGeoDa 0.9.9.12.5 (June 23, 2011)</label>
              <style>wxALIGN_CENTRE</style>
            </object>
            <flag>wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_OK">
              <label>OK</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_RANDOMIZATION" subclass="CRandomizationDlg">
    <object class="wxButton" name="ID_CLOSE">
      <size>50,15d</size>
      <pos>400,7d</pos>
      <label>&amp;Close</label>
    </object>
    <object class="wxButton" name="ID_OK">
      <size>50,15d</size>
      <pos>400,27d</pos>
      <label>&amp;Run</label>
    </object>
    <size>470,200d</size>
    <title>Randomization</title>
    <centered>1</centered>
    <style>wxCAPTION|wxCLOSE_BOX</style>
  </object>
  <object class="wxDialog" name="IDD_DIALOG_QUANTILE">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Quantile Map</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxHORIZONTAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxStaticBoxSizer" name="wxID_ANY">
          <orient>wxHORIZONTAL</orient>
          <label/>
          <object class="sizeritem">
            <object class="wxStaticText" name="IDC_STATIC">
              <label>Number of Classes</label>
            </object>
            <flag>wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
          </object>
          <object class="sizeritem">
            <object class="wxSpinCtrl" name="IDC_EDIT_QUANTILE"/>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_OK">
              <label>OK</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_VORONOI" subclass="CThiessenPolygonDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>SHAPE CONVERSION</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_LEFT|wxALL</flag>
        <border>5</border>
        <object class="wxFlexGridSizer">
          <cols>3</cols>
          <rows>2</rows>
          <vgap>0</vgap>
          <hgap>0</hgap>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="IDC_STATIC">
              <label>Input file (*.shp)</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxBitmapButton" name="IDC_BROWSE_IFILE">
              <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
              <bitmap stock_id="open-folder"/>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxTextCtrl" name="IDC_VORONOI_INFILE">
              <size>180,-1d</size>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="ID_STATICTEXT">
              <label>Output file (*.shp)</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxBitmapButton" name="IDC_BROWSE_OFILE">
              <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
              <bitmap stock_id="save"/>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxTextCtrl" name="IDC_VORONOI_OTFILE">
              <size>180,-1d</size>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_LEFT|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxCheckBox" name="IDC_REFERENCEFILE_CHK">
              <style>wxCHK_2STATE</style>
              <label>Bounding Box Reference  file (*.shp) </label>
              <checked>0</checked>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxHORIZONTAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_VORONOI_REFFILE">
                  <size>180,-1d</size>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBitmapButton" name="IDC_REFERENCEFILE">
                  <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
                  <bitmap stock_id="open-folder"/>
                </object>
              </object>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxHORIZONTAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDCREATE">
              <label>C&amp;reate</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDC_VOR_RESET">
              <label>Re&amp;set</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDCANCEL">
              <label>&amp;Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_INTERVALS" subclass="CHistIntervalDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Intervals in the Histogram</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxHORIZONTAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxStaticBoxSizer" name="wxID_ANY">
          <orient>wxHORIZONTAL</orient>
          <label/>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="IDC_STATIC">
              <label># of Intervals</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxTextCtrl" name="IDC_EDIT_INTERVAL">
              <style>wxTE_RIGHT</style>
              <value>7</value>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_OK">
              <label>OK</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_VAR_SETTING" subclass="CVariableSettingsDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Variables Settings</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxStaticBoxSizer" name="wxID_ANY">
          <orient>wxVERTICAL</orient>
          <label>Select Variables</label>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxHORIZONTAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBoxSizer">
                  <orient>wxVERTICAL</orient>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALL|wxADJUST_MINSIZE</flag>
                    <border>5</border>
                    <object class="wxStaticText" name="ID_STATICTEXT">
                      <label>1st Variable (X)</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxListBox" name="IDC_LIST_VARIABLE1">
                      <content/>
                      <size>119,68d</size>
                      <style>wxLB_SINGLE</style>
                    </object>
                  </object>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBoxSizer">
                  <orient>wxVERTICAL</orient>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALL|wxADJUST_MINSIZE</flag>
                    <border>5</border>
                    <object class="wxStaticText" name="IDC_STATIC_V2">
                      <label>2nd Variable (Y)</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxListBox" name="IDC_LIST_VARIABLE2">
                      <content/>
                      <size>119,68d</size>
                      <style>wxLB_SINGLE</style>
                    </object>
                  </object>
                </object>
              </object>
            </object>
          </object>
          <object class="sizeritem">
            <object class="wxCheckBox" name="ID_CHECKBOX">
              <label>Set the variables as default</label>
            </object>
            <flag>wxALL|wxALIGN_CENTRE</flag>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <object class="wxBoxSizer">
          <object class="sizeritem">
            <flag>wxALIGN_RIGHT|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDOK">
              <label>OK</label>
            </object>
          </object>
          <object class="sizeritem">
            <object class="wxButton" name="IDCANCEL">
              <label>Close</label>
            </object>
            <flag>wxALL|wxALIGN_LEFT</flag>
            <border>5</border>
          </object>
          <orient>wxHORIZONTAL</orient>
        </object>
        <flag>wxALL|wxALIGN_CENTRE_HORIZONTAL</flag>
        <border>5</border>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_SCATTER_PLOT_VARS" subclass="CScatterPlotVarsDlg">
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <object class="wxStaticBoxSizer" name="wxID_ANY">
          <object class="sizeritem">
            <object class="wxBoxSizer">
              <object class="sizeritem">
                <object class="wxBoxSizer">
                  <object class="sizeritem">
                    <object class="wxStaticText" name="ID_STATICTEXT_X">
                      <label>X (independent var)</label>
                    </object>
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALL|wxADJUST_MINSIZE</flag>
                    <border>5</border>
                  </object>
                  <object class="sizeritem">
                    <object class="wxListBox" name="ID_LIST_VAR_X">
                      <content/>
                      <size>100,90d</size>
                      <style>wxLB_SINGLE</style>
                    </object>
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                    <border>5</border>
                  </object>
                  <orient>wxVERTICAL</orient>
                </object>
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>2</border>
              </object>
              <object class="sizeritem">
                <object class="wxBoxSizer">
                  <object class="sizeritem">
                    <object class="wxStaticText" name="ID_STATICTEXT_Y">
                      <label>Y (dependent var)</label>
                    </object>
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALL|wxADJUST_MINSIZE</flag>
                    <border>5</border>
                  </object>
                  <object class="sizeritem">
                    <object class="wxListBox" name="ID_LIST_VAR_Y">
                      <content/>
                      <size>100,90d</size>
                      <style>wxLB_SINGLE</style>
                    </object>
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                    <border>5</border>
                  </object>
                  <orient>wxVERTICAL</orient>
                </object>
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>2</border>
              </object>
              <object class="sizeritem">
                <object class="wxBoxSizer">
                  <object class="sizeritem">
                    <object class="wxStaticText" name="ID_STATICTEXT_Z">
                      <label>Bubble size (optional)</label>
                    </object>
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALL|wxADJUST_MINSIZE</flag>
                    <border>5</border>
                  </object>
                  <object class="sizeritem">
                    <object class="wxListBox" name="ID_LIST_VAR_Z">
                      <content/>
                      <size>100,90d</size>
                      <style>wxLB_SINGLE</style>
                    </object>
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                    <border>5</border>
                  </object>
                  <orient>wxVERTICAL</orient>
                </object>
                <flag>wxALIGN_CENTRE_VERTICAL</flag>
                <border>2</border>
              </object>
              <orient>wxHORIZONTAL</orient>
            </object>
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>0</border>
          </object>
          <object class="sizeritem">
            <object class="wxBoxSizer">
              <object class="sizeritem">
                <object class="wxCheckBox" name="ID_SET_VARS_AS_DEFAULT">
                  <label>Set variables as default</label>
                </object>
                <flag>wxGROW|wxALIGN_CENTRE_VERTICAL</flag>
                <border>2</border>
              </object>
              <object class="spacer">
                <size>200,10</size>
                <flag>wxGROW|wxALIGN_CENTRE_VERTICAL</flag>
              </object>
              <object class="sizeritem">
                <object class="wxCheckBox" name="ID_INCLUDE_BUBBLE_SIZE">
                  <label>Include bubble size</label>
                </object>
                <flag>wxGROW|wxALIGN_CENTRE_VERTICAL</flag>
                <border>2</border>
              </object>
              <orient>wxHORIZONTAL</orient>
            </object>
            <flag>wxALIGN_CENTRE_HORIZONTAL</flag>
            <border>2</border>
            <ratio>100</ratio>
          </object>
          <label>Select Variables</label>
          <orient>wxVERTICAL</orient>
        </object>
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>3</border>
      </object>
      <object class="sizeritem">
        <object class="wxBoxSizer">
          <object class="sizeritem">
            <object class="wxButton" name="wxID_OK">
              <label>OK</label>
            </object>
            <flag>wxALIGN_RIGHT|wxALL</flag>
            <border>2</border>
          </object>
          <object class="spacer">
            <size>50,10</size>
            <flag>wxALIGN_CENTRE_VERTICAL</flag>
          </object>
          <object class="sizeritem">
            <object class="wxButton" name="wxID_CANCEL">
              <label>Cancel</label>
            </object>
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>2</border>
          </object>
          <orient>wxHORIZONTAL</orient>
        </object>
        <flag>wxALL|wxALIGN_CENTRE_HORIZONTAL</flag>
        <border>5</border>
      </object>
    </object>
    <title>Scatter Plot Variables</title>
    <centered>1</centered>
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
  </object>
  <object class="wxDialog" name="IDD_WEIGHT_CHARACTERISTICS">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>WEIGHT CHARACTERISTICS</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxStaticBoxSizer" name="wxID_ANY">
          <orient>wxVERTICAL</orient>
          <label/>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxHORIZONTAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="ID_STATICTEXT1">
                  <label>Open weights file</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="ID_STATICTEXT">
                  <label>(*.gal, *.gwt)</label>
                </object>
              </object>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxHORIZONTAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_EDIT_FILEWEIGHT">
                  <size>202,-1d</size>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBitmapButton" name="IDC_OPEN_FILEWEIGHT">
                  <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
                  <bitmap stock_id="open-folder"/>
                </object>
              </object>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxHORIZONTAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_OK">
              <label>OK</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_RATE_SMOOTHER">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Rate Smoothing</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxStaticBoxSizer" name="wxID_ANY">
          <orient>wxVERTICAL</orient>
          <label>Select Variables</label>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxHORIZONTAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBoxSizer">
                  <orient>wxVERTICAL</orient>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALL|wxADJUST_MINSIZE</flag>
                    <border>5</border>
                    <object class="wxStaticText" name="ID_STATICTEXT1">
                      <label>Event Variable</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxListBox" name="IDC_LIST_VARIABLE1">
                      <content/>
                      <size>119,68d</size>
                      <style>wxLB_SINGLE</style>
                    </object>
                  </object>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBoxSizer">
                  <orient>wxVERTICAL</orient>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALL|wxADJUST_MINSIZE</flag>
                    <border>5</border>
                    <object class="wxStaticText" name="IDC_STATIC_V2">
                      <label>Base Variable</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxListBox" name="IDC_LIST_VARIABLE2">
                      <content/>
                      <size>119,68d</size>
                      <style>wxLB_SINGLE</style>
                    </object>
                  </object>
                </object>
              </object>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxStaticBoxSizer" name="wxID_ANY">
          <orient>wxHORIZONTAL</orient>
          <label/>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="ID_STATICTEXT">
              <label>Map Themes</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxComboBox" name="IDC_COMBO_THEMATIC">
              <content/>
              <size>200,-1d</size>
              <style>wxCB_DROPDOWN</style>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_RIGHT|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_OK">
              <label>OK</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_GAUSS_EXIM" subclass="CDbf2GaussDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Exporting Data</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxHORIZONTAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="ID_STATICTEXT">
              <label>Input file name (*.dbf)</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxHORIZONTAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_EDIT_DBF">
                  <size>70,-1d</size>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBitmapButton" name="IDC_INPUTFILE">
                  <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
                  <bitmap stock_id="open-folder"/>
                </object>
              </object>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxListBox" name="IDC_LIST_VARIN">
              <content/>
              <size>90,107d</size>
              <style>wxLB_SINGLE</style>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_RIGHT|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDOK_EXPORT">
              <label>E&amp;xport</label>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDC_MOVEOUT_ALL">
              <label>&gt;&gt;</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDC_MOVEOUT_ONE">
              <label>&gt;</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDC_MOVEIN_ONE">
              <label>&lt;</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDC_MOVEIN_ALL">
              <label>&lt;&lt;</label>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="IDC_STATIC">
              <label>Output file name</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxHORIZONTAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_EDIT_DAT">
                  <size>70,-1d</size>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBitmapButton" name="IDC_OUTPUTFILE">
                  <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
                  <bitmap stock_id="save"/>
                </object>
              </object>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxListBox" name="IDC_LIST_VAROUT">
              <content/>
              <size>90,107d</size>
              <style>wxLB_SINGLE</style>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDOK_RESET">
              <label>&amp;Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_SELECT_WEIGHT">
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_LEFT|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxRadioButton" name="IDC_RADIO_OPENWEIGHT1">
              <label>Select from currently used</label>
              <style>wxRB_GROUP</style>
              <value>0</value>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxChoice" name="IDC_CURRENTUSED_W">
              <content/>
              <size>198,-1d</size>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_LEFT|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <object class="wxRadioButton" name="IDC_RADIO_OPENWEIGHT2">
              <label>Select from file (gal, gwt)</label>
            </object>
            <flag>wxALL|wxALIGN_LEFT</flag>
            <border>5</border>
          </object>
          <object class="sizeritem">
            <object class="wxBoxSizer">
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_EDIT_FILEWEIGHT">
                  <size>178,-1d</size>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBitmapButton" name="IDC_OPEN_FILEWEIGHT">
                  <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
                  <bitmap stock_id="open-folder"/>
                </object>
              </object>
              <orient>wxHORIZONTAL</orient>
            </object>
            <flag>wxALIGN_LEFT|wxALL</flag>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <object class="wxBoxSizer">
          <object class="sizeritem">
            <object class="wxStaticText">
              <label>Create new weights file:</label>
            </object>
            <flag>wxALIGN_CENTRE_VERTICAL</flag>
            <border>5</border>
          </object>
          <object class="spacer">
            <size>3,5d</size>
            <option>0</option>
          </object>
          <object class="sizeritem">
            <object class="wxBitmapButton" name="ID_CREATE_WEIGHTS">
              <bitmap stock_id="ToolBarBitmaps_4"/>
              <disabled stock_id="ToolBarBitmaps_4_disabled"/>
              <tooltip>Create new weights</tooltip>
            </object>
            <flag>wxALIGN_CENTRE_VERTICAL</flag>
          </object>
          <orient>wxHORIZONTAL</orient>
        </object>
        <flag>wxALL|wxALIGN_LEFT</flag>
        <border>5</border>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxHORIZONTAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_OK">
              <label>&amp;OK</label>
            </object>
          </object>
          <object class="spacer">
            <size>15,5d</size>
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>2</border>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>&amp;Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
    <title>Select Weights</title>
    <centered>1</centered>
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
  </object>
  <object class="wxDialog" name="IDD_WEIGHTS_FILE_CREATION">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Weights File Creation</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>2</border>
        <object class="wxStaticBoxSizer" name="wxID_ANY">
          <orient>wxVERTICAL</orient>
          <label/>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>2</border>
            <object class="wxBoxSizer">
              <orient>wxVERTICAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                <border>2</border>
                <object class="wxFlexGridSizer">
                  <cols>3</cols>
                  <rows>1</rows>
                  <vgap>0</vgap>
                  <hgap>0</hgap>
                  <object class="sizeritem">
                    <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                    <border>2</border>
                    <object class="wxStaticText" name="ID_INPUT_STAT_TXT">
                      <label>Input Shape File</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>2</border>
                    <object class="wxTextCtrl" name="ID_IN_SHP_TXT_CTRL">
                      <size>159,-1d</size>
                      <style>wxTE_READONLY</style>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>2</border>
                    <object class="wxBitmapButton" name="IDC_BROWSE_ISHP4W">
                      <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
                      <bitmap stock_id="open-folder"/>
                    </object>
                  </object>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALL</flag>
                <border>2</border>
                <object class="wxBoxSizer">
                  <orient>wxHORIZONTAL</orient>
                  <object class="sizeritem">
                    <object class="wxButton" name="ID_CREATE_ID">
                      <label>&amp;Add ID Variable...</label>
                    </object>
                    <flag>wxALL|wxALIGN_CENTRE</flag>
                    <border>2</border>
                  </object>
                  <object class="spacer">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>2</border>
                    <size>5,5d</size>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                    <border>2</border>
                    <object class="wxStaticText" name="ID_ID_VAR_STAT_TXT">
                      <label>Weights File ID Variable</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>2</border>
                    <object class="wxChoice" name="IDC_IDVARIABLE">
                      <content/>
                      <size>75,-1d</size>
                    </object>
                  </object>
                </object>
              </object>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>2</border>
            <object class="wxStaticBoxSizer" name="wxID_ANY">
              <orient>wxHORIZONTAL</orient>
              <label>Contiguity Weight</label>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>2</border>
                <object class="wxFlexGridSizer">
                  <cols>3</cols>
                  <rows>2</rows>
                  <vgap>0</vgap>
                  <hgap>0</hgap>
                  <object class="sizeritem">
                    <object class="wxRadioButton" name="IDC_RADIO_QUEEN">
                      <label>Queen Contiguity</label>
                      <value>0</value>
                      <style>wxRB_GROUP</style>
                    </object>
                    <flag>wxALIGN_LEFT</flag>
                    <border>2</border>
                  </object>
                  <object class="spacer">
                    <size>10,5d</size>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>2</border>
                    <object class="wxBoxSizer">
                      <orient>wxHORIZONTAL</orient>
                      <object class="sizeritem">
                        <flag>wxALIGN_RIGHT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                        <border>2</border>
                        <object class="wxStaticText" name="IDC_STATIC_OOC1">
                          <label>Order of contiguity</label>
                        </object>
                      </object>
                      <object class="sizeritem">
                        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                        <border>2</border>
                        <object class="wxTextCtrl" name="IDC_EDIT_ORDEROFCONTIGUITY">
                          <value>1</value>
                          <style>wxTE_READONLY|wxTE_RIGHT</style>
                        </object>
                      </object>
                      <object class="spacer">
                        <size>2,2</size>
                      </object>
                      <object class="sizeritem">
                        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                        <border>2</border>
                        <object class="wxSpinButton" name="IDC_SPIN_ORDEROFCONTIGUITY">
                          <style>wxSP_VERTICAL</style>
                          <value>0</value>
                          <min>0</min>
                          <max>100</max>
                        </object>
                      </object>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>2</border>
                    <object class="wxRadioButton" name="IDC_RADIO_ROOK">
                      <label>Rook Contiguity</label>
                      <value>0</value>
                    </object>
                  </object>
                  <object class="spacer">
                    <size>10,5d</size>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALL|wxALIGN_LEFT|wxALIGN_CENTRE_VERTICAL</flag>
                    <border>2</border>
                    <object class="wxCheckBox" name="IDC_CHECK1">
                      <style>wxCHK_2STATE</style>
                      <label>Include lower orders</label>
                      <checked>0</checked>
                    </object>
                  </object>
                </object>
              </object>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>2</border>
            <object class="wxStaticBoxSizer" name="wxID_ANY">
              <orient>wxVERTICAL</orient>
              <label>Distance Weight</label>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALL</flag>
                <border>2</border>
                <object class="wxFlexGridSizer">
                  <cols>2</cols>
                  <rows>3</rows>
                  <vgap>0</vgap>
                  <hgap>0</hgap>
                  <object class="sizeritem">
                    <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                    <border>2</border>
                    <object class="wxStaticText" name="IDC_STATIC3">
                      <label>Select distance metric</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>2</border>
                    <object class="wxChoice" name="IDC_DISTANCE_METRIC">
                      <content/>
                      <size>98,-1d</size>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                    <border>2</border>
                    <object class="wxStaticText" name="IDC_STATIC1">
                      <label>Variable for x-coordinates</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>2</border>
                    <object class="wxChoice" name="IDC_XCOORDINATES">
                      <content/>
                      <size>98,-1d</size>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                    <border>2</border>
                    <object class="wxStaticText" name="IDC_STATIC2">
                      <label>Variable for y-coordinates</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>2</border>
                    <object class="wxChoice" name="IDC_YCOORDINATES">
                      <content/>
                      <size>98,-1d</size>
                    </object>
                  </object>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALL</flag>
                <border>2</border>
                <object class="wxBoxSizer">
                  <orient>wxVERTICAL</orient>
                  <object class="sizeritem">
                    <flag>wxALIGN_LEFT|wxALL</flag>
                    <border>2</border>
                    <object class="wxBoxSizer">
                      <orient>wxHORIZONTAL</orient>
                      <object class="sizeritem">
                        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                        <border>2</border>
                        <object class="wxRadioButton" name="IDC_RADIO_DISTANCE">
                          <label>Threshold Distance</label>
                          <value>0</value>
                        </object>
                      </object>
                      <object class="spacer">
                        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                        <border>2</border>
                        <size>5,5d</size>
                      </object>
                      <object class="spacer">
                        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                        <border>2</border>
                        <size>5,5d</size>
                      </object>
                      <object class="sizeritem">
                        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                        <border>2</border>
                        <object class="wxTextCtrl" name="IDC_TRESHOLD_EDIT">
                          <style>wxTE_READONLY|wxTE_RIGHT</style>
                        </object>
                      </object>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_LEFT|wxALL</flag>
                    <border>2</border>
                    <object class="wxSlider" name="IDC_TRESHOLD_SLIDER">
                      <size>210,-1d</size>
                      <style>wxSL_HORIZONTAL</style>
                      <value>0</value>
                      <min>0</min>
                      <max>100</max>
                    </object>
                  </object>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALL</flag>
                <border>2</border>
                <object class="wxBoxSizer">
                  <orient>wxHORIZONTAL</orient>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>2</border>
                    <object class="wxRadioButton" name="IDC_RADIO_KNN">
                      <label>k-Nearest Neighbors</label>
                      <value>0</value>
                    </object>
                  </object>
                  <object class="spacer">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>2</border>
                    <size>5,5d</size>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                    <border>2</border>
                    <object class="wxStaticText" name="IDC_STATIC_KNN">
                      <label>Number of neighbors</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>2</border>
                    <object class="wxTextCtrl" name="IDC_EDIT_KNN">
                      <style>wxTE_READONLY|wxTE_RIGHT</style>
                    </object>
                  </object>
                  <object class="spacer">
                    <size>2,2</size>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>2</border>
                    <object class="wxSpinButton" name="IDC_SPIN_KNN">
                      <style>wxSP_VERTICAL</style>
                      <value>0</value>
                      <min>0</min>
                      <max>100</max>
                    </object>
                  </object>
                </object>
              </object>

            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxHORIZONTAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>2</border>
            <object class="wxButton" name="IDOK_CREATE1">
              <label>C&amp;reate</label>
            </object>
          </object>
          <object class="spacer">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>2</border>
            <size>5,5d</size>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>2</border>
            <object class="wxButton" name="wxID_CLOSE">
              <label>&amp;Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_ADD_ID_VARIABLE">
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <object class="wxStaticText" name="wxID_ANY">
              <label>Enter new ID variable name:</label>
            </object>
            <flag>wxALL|wxALIGN_CENTRE_HORIZONTAL</flag>
          </object>
          <object class="sizeritem">
            <object class="wxTextCtrl" name="IDC_NEW_ID_VAR">
              <value>POLY_ID</value>
              <size>90,-1d</size>
            </object>
            <flag>wxALL|wxALIGN_CENTRE_HORIZONTAL</flag>
            <border>5</border>
          </object>
        </object>
        <flag>wxALL|wxALIGN_LEFT</flag>
        <border>5</border>
      </object>
      <object class="sizeritem">
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <object class="wxStaticText" name="wxID_ANY">
              <label>Existing Variables</label>
            </object>
            <flag>wxALL|wxALIGN_CENTRE_HORIZONTAL</flag>
          </object>
          <object class="sizeritem">
            <object class="wxListBox" name="IDC_EXISTING_VARS_LIST">
              <content/>
              <size>90,100d</size>
            </object>
            <flag>wxALL|wxALIGN_CENTRE_HORIZONTAL</flag>
            <border>5</border>
          </object>
        </object>
        <flag>wxALL|wxALIGN_LEFT</flag>
        <border>5</border>
      </object>
      <object class="sizeritem">
        <object class="wxBoxSizer">
          <orient>wxHORIZONTAL</orient>
          <object class="sizeritem">
            <object class="wxButton" name="wxID_OK">
              <label>Save to DBF File</label>
            </object>
            <flag>wxALL|wxALIGN_CENTRE_VERTICAL</flag>
            <border>5</border>
          </object>
          <object class="sizeritem">
            <object class="wxButton" name="wxID_CANCEL">
              <label>Cancel</label>
            </object>
            <flag>wxALL|wxALIGN_CENTRE_VERTICAL</flag>
            <border>5</border>
          </object>
        </object>
        <flag>wxALL|wxALIGN_CENTRE_HORIZONTAL</flag>
        <border>5</border>
      </object>
    </object>
    <title>Add New ID Variable</title>
    <centered>1</centered>
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
  </object>
  <object class="wxDialog" name="IDD_ADD_CENTROIDS" subclass="CAddCentroidsDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>EXPORT CENTROIDS-&gt;DBF</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxStaticBoxSizer" name="wxID_ANY">
          <orient>wxVERTICAL</orient>
          <label/>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxFlexGridSizer">
              <cols>3</cols>
              <rows>3</rows>
              <vgap>0</vgap>
              <hgap>0</hgap>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="IDC_STATIC">
                  <label>Shape file (*.shp)</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_EDIT_FILEWEIGHT">
                  <size>172,-1d</size>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBitmapButton" name="IDC_OPEN_ISHAPE">
                  <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
                  <bitmap stock_id="open-folder"/>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="ID_STATICTEXT2">
                  <label>Output file (*.dbf)</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_EDIT_ODBF">
                  <size>172,-1d</size>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBitmapButton" name="IDC_OPEN_ODBF">
                  <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
                  <bitmap stock_id="save"/>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_RIGHT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="ID_STATICTEXT">
                  <label>Key Variable</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxChoice" name="IDC_KEYVAR">
                  <content/>
                  <size>130,-1d</size>
                </object>
              </object>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxHORIZONTAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDOK_ADD">
              <label>C&amp;reate</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDCANCEL">
              <label>&amp;Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_ADD_MEANCENTERS" subclass="CAddCentroidsDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>EXPORT MEAN CENTERS-&gt;DBF</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxStaticBoxSizer" name="wxID_ANY">
          <orient>wxVERTICAL</orient>
          <label/>
          <object class="sizeritem">
            <object class="wxFlexGridSizer">
              <cols>3</cols>
              <rows>3</rows>
              <vgap>0</vgap>
              <hgap>0</hgap>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="IDC_STATIC">
                  <label>Shape file (*.shp)</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_EDIT_FILEWEIGHT">
                  <size>172,-1d</size>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBitmapButton" name="IDC_OPEN_ISHAPE">
                  <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
                  <bitmap stock_id="open-folder"/>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="ID_STATICTEXT2">
                  <label>Output file (*.dbf)</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_EDIT_ODBF">
                  <size>172,-1d</size>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBitmapButton" name="IDC_OPEN_ODBF">
                  <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
                  <bitmap stock_id="save"/>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_RIGHT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="ID_STATICTEXT">
                  <label>Key Variable</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxChoice" name="IDC_KEYVAR">
                  <content/>
                  <size>130,-1d</size>
                </object>
              </object>
              <object class="spacer">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <size>5,5d</size>
              </object>
            </object>
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxHORIZONTAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDOK_ADD">
              <label>C&amp;reate</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDCANCEL">
              <label>&amp;Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_RANGE_SETTING2" subclass="CRangeSettingDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Range Selection</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_LEFT|wxALL</flag>
        <border>5</border>
        <object class="wxStaticBoxSizer" name="wxID_ANY">
          <orient>wxHORIZONTAL</orient>
          <label>Range Selection</label>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxTextCtrl" name="IDC_MIN"/>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="IDC_STATIC">
              <label>&lt;=</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxChoice" name="IDC_FIELD">
              <content/>
              <size>90,-1d</size>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="ID_STATICTEXT1">
              <label>&lt;</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxTextCtrl" name="IDC_MAX">
              <size>43,-1d</size>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDOK2">
              <label>&amp;Apply</label>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxGROW|wxALL</flag>
        <border>5</border>
        <object class="wxStaticBoxSizer" name="wxID_ANY">
          <orient>wxHORIZONTAL</orient>
          <label>Recording</label>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxComboBox" name="IDC_FIELD2">
              <content/>
              <size>90,-1d</size>
              <style>wxCB_DROPDOWN</style>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="ID_STATICTEXT">
              <label>=</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxTextCtrl" name="IDC_EDIT_SPIN">
              <size>26,-1d</size>
              <value>1</value>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDOK3">
              <label>Appl&amp;y</label>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_RIGHT|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxHORIZONTAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDOK">
              <label>&amp;OK</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>&amp;Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_DELETE_COLUMN" subclass="CDeleteColumnDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Remove Column</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxHORIZONTAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="IDC_STATIC">
              <label>Pick the column name</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxChoice" name="IDC_COMBO1">
              <content/>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDOK">
              <label>Delete</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_ADD_COLUMN" subclass="CAddColumnDlg">
    <object class="wxBoxSizer">
      <orient>wxHORIZONTAL</orient>
      <object class="sizeritem">
        <object class="wxFlexGridSizer">
          <object class="sizeritem">
            <object class="wxStaticText" name="ID_STATIC_TEXT1">
              <label>Name</label>
            </object>
            <flag>wxALIGN_CENTRE_VERTICAL</flag>
          </object>
          <object class="sizeritem">
            <object class="wxTextCtrl" name="IDC_EDIT1">
              <size>110,13d</size>
            </object>
            <flag>wxALIGN_CENTRE_VERTICAL</flag>
          </object>
          <object class="sizeritem">
            <object class="wxStaticText" name="ID_STATIC_TEXT2">
              <label>Type</label>
            </object>
          </object>
          <object class="sizeritem">
            <object class="wxChoice" name="IDC_COMBO_TYPE">
              <content/>
            </object>
          </object>
          <object class="sizeritem">
            <object class="wxStaticText" name="IDC_STATIC_TEXT3">
              <label>After</label>
            </object>
          </object>
          <object class="sizeritem">
            <object class="wxChoice" name="IDC_COMBO1">
              <content/>
            </object>
          </object>
          <cols>2</cols>
          <rows>3</rows>
          <vgap>5</vgap>
          <hgap>5</hgap>
        </object>
        <flag>wxALL|wxALIGN_CENTRE_VERTICAL</flag>
        <border>8</border>
        <minsize>100,200d</minsize>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <object class="wxButton" name="wxID_OK">
              <label>Add</label>
            </object>
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
    <title>Add Column</title>
    <centered>1</centered>
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
  </object>
  <object class="wxDialog" name="IDD_CONVERT_DBF2SHP" subclass="CDBF2SHPDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Convert DBF to SHP</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxStaticBoxSizer" name="wxID_ANY">
          <orient>wxVERTICAL</orient>
          <label/>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxFlexGridSizer">
              <cols>3</cols>
              <rows>2</rows>
              <vgap>0</vgap>
              <hgap>0</hgap>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="IDC_STATIC">
                  <label>Input file (*.dbf)</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_FIELD_DBF">
                  <size>172,-1d</size>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBitmapButton" name="IDC_OPEN_IDBF">
                  <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
                  <bitmap stock_id="open-folder"/>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="ID_STATICTEXT2">
                  <label>Output file (*.shp)</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_FIELD_SHP">
                  <size>172,-1d</size>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBitmapButton" name="IDC_OPEN_OSHP">
                  <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
                  <bitmap stock_id="save"/>
                </object>
              </object>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxHORIZONTAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBoxSizer">
                  <orient>wxHORIZONTAL</orient>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                    <border>5</border>
                    <object class="wxStaticText" name="ID_STATICTEXT1">
                      <size>26,8d</size>
                      <pos>20,65d</pos>
                      <label>X-coord</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxChoice" name="IDC_KEYVAR">
                      <content/>
                      <size>77,-1d</size>
                    </object>
                  </object>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBoxSizer">
                  <orient>wxHORIZONTAL</orient>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                    <border>5</border>
                    <object class="wxStaticText" name="ID_STATICTEXT">
                      <size>26,8d</size>
                      <pos>158,66d</pos>
                      <label>Y-coord</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxChoice" name="IDC_KEYVAR2">
                      <content/>
                      <size>77,-1d</size>
                    </object>
                  </object>
                </object>
              </object>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxHORIZONTAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDOK_ADD">
              <label>C&amp;reate</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDOKDONE">
              <label>&amp;Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_CONVERT_ASC2SHP" subclass="CASC2SHPDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Convert ASC to SHP</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxStaticBoxSizer" name="wxID_ANY">
          <orient>wxVERTICAL</orient>
          <label/>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxFlexGridSizer">
              <cols>3</cols>
              <rows>2</rows>
              <vgap>0</vgap>
              <hgap>0</hgap>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="IDC_STATIC">
                  <label>Input file (text file)</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_FIELD_ASC">
                  <size>172,-1d</size>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBitmapButton" name="IDC_OPEN_IASC">
                  <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
                  <bitmap stock_id="open-folder"/>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="ID_STATICTEXT2">
                  <label>Output file (*.shp)</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_FIELD_SHP">
                  <size>172,-1d</size>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBitmapButton" name="IDC_OPEN_OSHP">
                  <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
                  <bitmap stock_id="save"/>
                </object>
              </object>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxHORIZONTAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBoxSizer">
                  <orient>wxHORIZONTAL</orient>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                    <border>5</border>
                    <object class="wxStaticText" name="ID_STATICTEXT1">
                      <label>X-coord</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxChoice" name="IDC_KEYVAR">
                      <content/>
                      <size>77,-1d</size>
                    </object>
                  </object>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBoxSizer">
                  <orient>wxHORIZONTAL</orient>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                    <border>5</border>
                    <object class="wxStaticText" name="ID_STATICTEXT">
                      <label>Y-coord</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxChoice" name="IDC_KEYVAR2">
                      <content/>
                      <size>77,-1d</size>
                    </object>
                  </object>
                </object>
              </object>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxHORIZONTAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDOK_ADD">
              <label>C&amp;reate</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDCANCEL">
              <label>&amp;Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_CONVERT_SHP2ASC" subclass="CSHP2ASCDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Exporting Shape to Boundary</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxHORIZONTAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxStaticBoxSizer" name="wxID_ANY">
              <orient>wxVERTICAL</orient>
              <label/>
              <object class="sizeritem">
                <object class="wxFlexGridSizer">
                  <object class="sizeritem">
                    <object class="wxStaticText" name="ID_STATICTEXT3">
                      <label>Input file (*.shp)</label>
                    </object>
                    <flag>wxALL|wxALIGN_LEFT</flag>
                    <border>5</border>
                  </object>
                  <object class="sizeritem">
                    <object class="wxTextCtrl" name="IDC_FIELD_SHP">
                      <size>172,-1d</size>
                    </object>
                    <flag>wxALL|wxALIGN_LEFT</flag>
                    <border>5</border>
                  </object>
                  <object class="sizeritem">
                    <object class="wxBitmapButton" name="IDC_OPEN_ISHP">
                      <bitmap stock_id="open-folder"/>
                      <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
                    </object>
                    <flag>wxALL|wxALIGN_LEFT</flag>
                    <border>5</border>
                  </object>
                  <object class="sizeritem">
                    <object class="wxStaticText" name="ID_STATICTEXT2">
                      <label>Output file (text file)</label>
                    </object>
                    <flag>wxALL|wxALIGN_LEFT</flag>
                    <border>5</border>
                  </object>
                  <object class="sizeritem">
                    <object class="wxTextCtrl" name="IDC_FIELD_ASC">
                      <size>172,-1d</size>
                    </object>
                    <flag>wxALL|wxALIGN_LEFT</flag>
                    <border>5</border>
                  </object>
                  <object class="sizeritem">
                    <object class="wxBitmapButton" name="IDC_OPEN_OASC">
                      <bitmap stock_id="save"/>
                      <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
                    </object>
                    <flag>wxALL|wxALIGN_LEFT</flag>
                    <border>5</border>
                  </object>
                  <object class="sizeritem">
                    <object class="wxStaticText" name="ID_STATICTEXT4">
                      <label>Key</label>
                    </object>
                    <flag>wxALL|wxALIGN_RIGHT</flag>
                    <border>5</border>
                  </object>
                  <object class="sizeritem">
                    <object class="wxChoice" name="IDC_KEYVAR">
                      <content/>
                      <size>77,-1d</size>
                    </object>
                    <flag>wxALL|wxALIGN_LEFT</flag>
                    <border>5</border>
                  </object>
                  <object class="spacer">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                    <size>5,5d</size>
                  </object>
                  <cols>3</cols>
                  <rows>3</rows>
                  <vgap>0</vgap>
                  <hgap>0</hgap>
                </object>
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                <border>5</border>
              </object>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxHORIZONTAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxButton" name="IDOK_ADD">
                  <label>C&amp;reate</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxButton" name="IDOKDONE">
                  <label>&amp;Close</label>
                </object>
              </object>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_TOP|wxALL</flag>
        <border>5</border>
        <object class="wxStaticBoxSizer" name="wxID_ANY">
          <orient>wxVERTICAL</orient>
          <label>Format Type</label>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxFlexGridSizer">
              <cols>2</cols>
              <rows>2</rows>
              <vgap>0</vgap>
              <hgap>0</hgap>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxRadioButton" name="IDC_RADIO1">
                  <label>Type 1</label>
                  <style>wxRB_GROUP</style>
                  <value>0</value>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_RIGHT|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxRadioButton" name="IDC_RADIO2">
                  <label>Type 1a</label>
                  <value>0</value>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxRadioButton" name="IDC_RADIO3">
                  <label>Type 2</label>
                  <value>0</value>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_RIGHT|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxRadioButton" name="IDC_RADIO4">
                  <label>Type 2a</label>
                  <value>0</value>
                </object>
              </object>
            </object>
          </object>
          <object class="spacer">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <size>5,5d</size>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="ID_STATICTEXT">
              <label>Produce bounding-box file?</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxCheckBox" name="IDC_CHECK1">
              <style>wxCHK_2STATE</style>
              <label>Yes</label>
              <checked>0</checked>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_SAVE_LISA" subclass="CSaveLisaDlg">
    <object class="wxBoxSizer">
      <object class="sizeritem">
        <object class="wxFlexGridSizer">
          <object class="sizeritem">
            <object class="wxCheckBox" name="IDC_CHECK1">
              <size>85,-1d</size>
              <label>Lisa Indices</label>
            </object>
            <flag>wxALIGN_CENTRE_VERTICAL</flag>
          </object>
          <object class="sizeritem">
            <object class="wxComboBox" name="IDC_COMBO1">
              <content/>
              <size>85,-1d</size>
              <style>wxCB_DROPDOWN</style>
            </object>
            <flag>wxALIGN_CENTRE_VERTICAL</flag>
          </object>
          <object class="sizeritem">
            <object class="wxCheckBox" name="IDC_CHECK2">
              <size>85,-1d</size>
              <label>Clusters</label>
            </object>
            <flag>wxALIGN_CENTRE_VERTICAL</flag>
          </object>
          <object class="sizeritem">
            <object class="wxComboBox" name="IDC_COMBO2">
              <content/>
              <size>85,-1d</size>
              <style>wxCB_DROPDOWN</style>
            </object>
            <flag>wxALIGN_CENTRE_VERTICAL</flag>
          </object>
          <object class="sizeritem">
            <object class="wxCheckBox" name="IDC_CHECK3">
              <size>85,-1d</size>
              <label>Significances</label>
            </object>
            <flag>wxALIGN_CENTRE_VERTICAL</flag>
          </object>
          <object class="sizeritem">
            <object class="wxComboBox" name="IDC_COMBO3">
              <content/>
              <size>85,-1d</size>
              <style>wxCB_DROPDOWN</style>
            </object>
            <flag>wxALIGN_CENTRE_VERTICAL</flag>
          </object>
          <cols>2</cols>
          <rows>3</rows>
        </object>
        <flag>wxALL</flag>
        <border>8</border>
      </object>
      <object class="sizeritem">
        <object class="wxBoxSizer">
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_OK">
              <label>OK</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>Close</label>
            </object>
          </object>
          <orient>wxHORIZONTAL</orient>
        </object>
        <flag>wxALL|wxALIGN_CENTRE</flag>
        <border>5</border>
      </object>
      <orient>wxVERTICAL</orient>
    </object>
    <title>Save LISA Results</title>
    <centered>1</centered>
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
  </object>
  <object class="wxDialog" name="IDD_SAVE_GETIS_ORD" subclass="SaveGetisOrdDlg">
    <object class="wxBoxSizer">
      <object class="sizeritem">
        <object class="wxFlexGridSizer">
          <object class="sizeritem">
            <object class="wxCheckBox" name="IDC_CHECK1">
              <size>85,-1d</size>
              <label>Indices</label>
            </object>
            <flag>wxALIGN_CENTRE_VERTICAL</flag>
          </object>
          <object class="sizeritem">
            <object class="wxComboBox" name="IDC_COMBO1">
              <content/>
              <size>85,-1d</size>
              <style>wxCB_DROPDOWN</style>
            </object>
            <flag>wxALIGN_CENTRE_VERTICAL</flag>
          </object>
          <object class="sizeritem">
            <object class="wxCheckBox" name="IDC_CHECK2">
              <size>85,-1d</size>
              <label>Clusters</label>
            </object>
            <flag>wxALIGN_CENTRE_VERTICAL</flag>
          </object>
          <object class="sizeritem">
            <object class="wxComboBox" name="IDC_COMBO2">
              <content/>
              <size>85,-1d</size>
              <style>wxCB_DROPDOWN</style>
            </object>
            <flag>wxALIGN_CENTRE_VERTICAL</flag>
          </object>
          <object class="sizeritem">
            <object class="wxCheckBox" name="IDC_CHECK3">
              <size>85,-1d</size>
              <label>Significances</label>
            </object>
            <flag>wxALIGN_CENTRE_VERTICAL</flag>
          </object>
          <object class="sizeritem">
            <object class="wxComboBox" name="IDC_COMBO3">
              <content/>
              <size>85,-1d</size>
              <style>wxCB_DROPDOWN</style>
            </object>
            <flag>wxALIGN_CENTRE_VERTICAL</flag>
          </object>
          <cols>2</cols>
          <rows>3</rows>
        </object>
        <flag>wxALL</flag>
        <border>8</border>
      </object>
      <object class="sizeritem">
        <object class="wxBoxSizer">
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_OK">
              <label>OK</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>Close</label>
            </object>
          </object>
          <orient>wxHORIZONTAL</orient>
        </object>
        <flag>wxALL|wxALIGN_CENTRE</flag>
        <border>5</border>
      </object>
      <orient>wxVERTICAL</orient>
    </object>
    <title>Save Local G Stats Results</title>
    <centered>1</centered>
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
  </object>
  <object class="wxDialog" name="IDD_PERMUTATION_COUNT" subclass="CPermutationCounterDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Set Number of Permutation</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxHORIZONTAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxTextCtrl" name="IDC_EDIT_ORDEROFCONTIGUITY"/>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_OK">
              <label>OK</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_LISAWINDOWS2OPEN" subclass="CLisaWhat2OpenDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>What windows to open?</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxHORIZONTAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxCheckBox" name="IDC_CHECK1">
              <style>wxCHK_2STATE</style>
              <label>Significance Map</label>
              <checked>0</checked>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxCheckBox" name="IDC_CHECK2">
              <style>wxCHK_2STATE</style>
              <label>Cluster Map </label>
              <checked>0</checked>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxCheckBox" name="IDC_CHECK3">
              <style>wxCHK_2STATE</style>
              <label>Box Plot</label>
              <checked>0</checked>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxCheckBox" name="IDC_CHECK4">
              <style>wxCHK_2STATE</style>
              <label>Moran Scatter Plot</label>
              <checked>0</checked>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_TOP|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_OK">
              <label>OK</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_GETIS_ORD_CHOICE" subclass="GetisOrdChoiceDlg">
    <object class="wxBoxSizer">
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <object class="wxCheckBox" name="IDC_GI_CHECK">
              <label>Gi cluster map, pseudo p-val</label>
              <checked>1</checked>
            </object>
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
          </object>
          <object class="sizeritem">
            <object class="wxCheckBox" name="IDC_GI_STAR_CHECK">
              <label>Gi* cluster map, pseudo p-val</label>
            </object>
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
          </object>
          <object class="spacer">
            <size>5,5d</size>
          </object>
          <object class="sizeritem">
            <object class="wxCheckBox" name="IDC_SIG_MAPS_CHECK">
              <label>show significance maps</label>
            </object>
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
          </object>
          <object class="sizeritem">
            <object class="wxCheckBox" name="IDC_NORM_P_VAL_CHECK">
              <label>show normal distribution p-val maps</label>
            </object>
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
          </object>
          <object class="spacer">
            <size>5,5d</size>
          </object>
          <object class="sizeritem">
            <object class="wxBoxSizer">
              <object class="sizeritem">
                <object class="wxStaticText">
                  <label>weights:</label>
                </object>
              </object>
              <object class="spacer">
                <size>3,3d</size>
              </object>
              <object class="sizeritem">
                <object class="wxRadioButton" name="IDC_W_ROW_STAND">
                  <style>wxRB_GROUP</style>
                  <value>1</value>
                </object>
              </object>
              <object class="sizeritem">
                <object class="wxStaticText">
                  <label>row-standardized</label>
                </object>
              </object>
              <object class="spacer">
                <size>5,5d</size>
              </object>
              <object class="sizeritem">
                <object class="wxRadioButton" name="IDC_W_BINARY">
                  <value>0</value>
                </object>
              </object>
              <object class="sizeritem">
                <object class="wxStaticText">
                  <label>binary</label>
                </object>
              </object>
              <orient>wxHORIZONTAL</orient>
            </object>
            <flag>wxALL</flag>
            <border>5</border>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <object class="wxBoxSizer">
          <object class="sizeritem">
            <object class="wxButton" name="wxID_OK">
              <label>OK</label>
            </object>
            <flag>wxALL|wxALIGN_CENTRE_VERTICAL</flag>
            <border>5</border>
          </object>
          <object class="sizeritem">
            <object class="wxButton" name="wxID_CANCEL">
              <label>Close</label>
            </object>
            <flag>wxALL|wxALIGN_CENTRE_VERTICAL</flag>
            <border>5</border>
          </object>
          <orient>wxHORIZONTAL</orient>
        </object>
        <flag>wxALL|wxALIGN_TOP|wxALIGN_CENTRE_HORIZONTAL</flag>
        <border>5</border>
      </object>
      <orient>wxVERTICAL</orient>
    </object>
    <title>Local G Statistics Maps</title>
    <centered>1</centered>
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
  </object>
  <object class="wxDialog" name="IDD_MERGE_TABLE" subclass="CJoinTableDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Merge Table Data</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxStaticBoxSizer" name="wxID_ANY">
          <orient>wxVERTICAL</orient>
          <label/>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxFlexGridSizer">
              <cols>3</cols>
              <rows>2</rows>
              <vgap>0</vgap>
              <hgap>0</hgap>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="ID_STATICTEXT21">
                  <label>Input file (*.dbf)</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_FIELD_DBF">
                  <size>165,-1d</size>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBitmapButton" name="IDC_OPEN_IDBF">
                  <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
                  <bitmap stock_id="open-folder"/>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_RIGHT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="ID_STATICTEXT">
                  <label>Key</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxChoice" name="IDC_KEYVAR">
                  <content/>
                  <size>100,-1d</size>
                </object>
              </object>
              <object class="spacer">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <size>5,5d</size>
              </object>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxFlexGridSizer">
          <cols>3</cols>
          <rows>2</rows>
          <vgap>0</vgap>
          <hgap>0</hgap>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="ID_STATICTEXT4">
              <label>Do not include</label>
            </object>
          </object>
          <object class="spacer">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <size>5,5d</size>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="ID_STATICTEXT3">
              <label>Include</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxListBox" name="IDC_LIST_VARIN">
              <content/>
              <size>90,107d</size>
              <style>wxLB_SINGLE</style>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxVERTICAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                <border>5</border>
                <object class="wxButton" name="IDC_MOVEOUT_ALL">
                  <label>&gt;&gt;</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                <border>5</border>
                <object class="wxButton" name="IDC_MOVEOUT_ONE">
                  <label>&gt;</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                <border>5</border>
                <object class="wxButton" name="IDC_MOVEIN_ONE">
                  <label>&lt;</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                <border>5</border>
                <object class="wxButton" name="IDC_MOVEIN_ALL">
                  <label>&lt;&lt;</label>
                </object>
              </object>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxListBox" name="IDC_LIST_VAROUT">
              <content/>
              <size>90,107d</size>
              <style>wxLB_SINGLE</style>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxHORIZONTAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDOK">
              <label>&amp;Merge</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxPanel" name="IDD_FIELDCALC_UN" subclass="CFieldCalcUniDlg">
    <object class="wxBoxSizer">
      <orient>wxHORIZONTAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <object class="wxBoxSizer">
              <object class="sizeritem">
                <object class="wxStaticText" name="ID_STATICTEXT5">
                  <label>Result</label>
                </object>
                <flag>wxALIGN_CENTRE_VERTICAL</flag>
              </object>
              <object class="spacer">
                <size>5,5d</size>
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>2</border>
              </object>
              <object class="sizeritem">
                <object class="wxButton" name="ID_ADD_COLUMN">
                  <label>Add Column</label>
                  <tooltip>Add new column to table</tooltip>
                </object>
                <flag>wxALIGN_CENTRE_VERTICAL</flag>
              </object>
              <orient>wxHORIZONTAL</orient>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxChoice" name="IDC_UNARY_RESULT">
              <content/>
            </object>
          </object>
          <object class="spacer">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
        <border>5</border>
        <object class="wxStaticText" name="ID_STATICTEXT">
          <label>=</label>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxHORIZONTAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBoxSizer">
                  <orient>wxVERTICAL</orient>
                  <object class="sizeritem">
                    <flag>wxALIGN_LEFT|wxALL|wxADJUST_MINSIZE</flag>
                    <border>5</border>
                    <object class="wxStaticText" name="ID_STATICTEXT2">
                      <label>Operators</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_LEFT|wxALL</flag>
                    <border>5</border>
                    <object class="wxChoice" name="IDC_UNARY_OPERATOR">
                      <content/>
                    </object>
                  </object>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBoxSizer">
                  <orient>wxVERTICAL</orient>
                  <object class="sizeritem">
                    <flag>wxALIGN_LEFT|wxALL|wxADJUST_MINSIZE</flag>
                    <border>5</border>
                    <object class="wxStaticText" name="ID_STATICTEXT3">
                      <label>Variables</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_LEFT|wxALL</flag>
                    <border>5</border>
                    <object class="wxChoice" name="IDC_UNARY_OPERAND">
                      <content/>
                    </object>
                  </object>
                </object>
              </object>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxGROW|wxALL</flag>
            <border>5</border>
            <object class="wxTextCtrl" name="IDC_EDIT1"/>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxPanel" name="IDD_FIELDCALC_BI" subclass="CFieldCalcBinDlg">
    <object class="wxBoxSizer">
      <orient>wxHORIZONTAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <object class="wxBoxSizer">
              <object class="sizeritem">
                <object class="wxStaticText" name="ID_STATICTEXT2">
                  <label>Result</label>
                </object>
                <flag>wxALIGN_CENTRE_VERTICAL</flag>
              </object>
              <object class="spacer">
                <size>5,5d</size>
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>2</border>
              </object>
              <orient>wxHORIZONTAL</orient>
              <object class="sizeritem">
                <object class="wxButton" name="ID_ADD_COLUMN">
                  <label>Add Column</label>
                  <tooltip>Add new column to table</tooltip>
                </object>
              </object>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxChoice" name="IDC_BINARY_RESULT">
              <content/>
            </object>
          </object>
          <object class="spacer">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
        <border>5</border>
        <object class="wxStaticText" name="ID_STATICTEXT">
          <label>=</label>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxHORIZONTAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBoxSizer">
                  <orient>wxVERTICAL</orient>
                  <object class="sizeritem">
                    <flag>wxALIGN_LEFT|wxALL|wxADJUST_MINSIZE</flag>
                    <border>5</border>
                    <object class="wxStaticText" name="ID_STATICTEXT3">
                      <label>Variables-1</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxChoice" name="IDC_BINARY_OPERAND1">
                      <content/>
                    </object>
                  </object>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBoxSizer">
                  <orient>wxVERTICAL</orient>
                  <object class="sizeritem">
                    <flag>wxALIGN_LEFT|wxALL|wxADJUST_MINSIZE</flag>
                    <border>5</border>
                    <object class="wxStaticText" name="ID_STATICTEXT4">
                      <label>Operators</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxChoice" name="IDC_BINARY_OPERATOR">
                      <content/>
                    </object>
                  </object>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBoxSizer">
                  <orient>wxVERTICAL</orient>
                  <object class="sizeritem">
                    <flag>wxALIGN_LEFT|wxALL|wxADJUST_MINSIZE</flag>
                    <border>5</border>
                    <object class="wxStaticText" name="IDC_STATIC">
                      <label>Variables-2</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxChoice" name="IDC_BINARY_OPERAND2">
                      <content/>
                    </object>
                  </object>
                </object>
              </object>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxGROW|wxALL</flag>
            <border>5</border>
            <object class="wxTextCtrl" name="IDC_EDIT5"/>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxPanel" name="IDD_FIELDCALC_LAG" subclass="CFieldCalcLagDlg">
    <object class="wxBoxSizer">
      <orient>wxHORIZONTAL</orient>
      <object class="sizeritem">
        <object class="wxBoxSizer">
          <object class="sizeritem">
            <object class="wxBoxSizer">
              <object class="sizeritem">
                <object class="wxStaticText" name="ID_STATICTEXT4">
                  <label>Result</label>
                </object>
                <flag>wxALIGN_CENTRE_VERTICAL</flag>
              </object>
              <object class="spacer">
                <size>5,5d</size>
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>2</border>
              </object>
              <object class="sizeritem">
                <object class="wxButton" name="ID_ADD_COLUMN">
                  <label>Add Column</label>
                  <tooltip>Add new column to table</tooltip>
                </object>
              </object>
              <orient>wxHORIZONTAL</orient>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxChoice" name="IDC_LAG_RESULT">
              <content/>
            </object>
          </object>
          <object class="spacer">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
          </object>
          <orient>wxVERTICAL</orient>
        </object>
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
        <border>5</border>
        <object class="wxStaticText" name="ID_STATICTEXT2">
          <label>=</label>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <object class="wxBoxSizer">
              <object class="sizeritem">
                <object class="wxBoxSizer">
                  <orient>wxHORIZONTAL</orient>
                  <object class="sizeritem">
                    <object class="wxStaticText" name="ID_STATICTEXT3">
                      <label>Weights files</label>
                    </object>
                    <flag>wxALIGN_CENTRE_VERTICAL</flag>
                  </object>
                  <object class="spacer">
                    <size>5,5d</size>
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>2</border>
                  </object>
                  <object class="sizeritem">
                    <object class="wxBitmapButton" name="ID_OPEN_WEIGHT">
                      <bitmap stock_id="ToolBarBitmaps_3"/>
                      <disabled stock_id="ToolBarBitmaps_3_disabled"/>
                      <tooltip>Open weights file</tooltip>
                    </object>
                    <flag>wxALIGN_CENTRE_VERTICAL</flag>
                  </object>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxGROW|wxALL</flag>
                <border>5</border>
                <object class="wxChoice" name="IDC_CURRENTUSED_W">
                  <content/>
                </object>
              </object>
              <orient>wxVERTICAL</orient>
            </object>
            <flag>wxALL|wxALIGN_LEFT</flag>
          </object>
          <object class="sizeritem">
            <object class="wxBoxSizer">
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="IDC_STATIC">
                  <label>Variables</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALL</flag>
                <border>5</border>
                <object class="wxChoice" name="IDC_LAG_OPERAND">
                  <content/>
                </object>
              </object>
              <orient>wxVERTICAL</orient>
            </object>
            <flag>wxALL|wxALIGN_LEFT</flag>
          </object>
          <object class="sizeritem">
            <object class="wxTextCtrl" name="IDC_EDIT6">
              <size>320,-1d</size>
            </object>
            <flag>wxALL|wxGROW|wxALIGN_LEFT</flag>
            <border>5</border>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxPanel" name="IDD_FIELDCALC_RATE" subclass="CFieldCalcRateDlg">
    <object class="wxFlexGridSizer">
      <cols>3</cols>
      <rows>2</rows>
      <vgap>0</vgap>
      <hgap>0</hgap>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <object class="wxBoxSizer">
              <object class="sizeritem">
                <object class="wxStaticText" name="ID_STATICTEXT">
                  <label>Result</label>
                </object>
                <flag>wxALIGN_CENTRE_VERTICAL</flag>
              </object>
              <object class="spacer">
                <size>5,5d</size>
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>2</border>
              </object>
              <orient>wxHORIZONTAL</orient>
              <object class="sizeritem">
                <object class="wxButton" name="ID_ADD_COLUMN">
                  <label>Add Column</label>
                  <tooltip>Add new column to table</tooltip>
                </object>
              </object>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxChoice" name="IDC_RATE_RESULT">
              <content/>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="spacer">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="ID_STATICTEXT2">
              <label>=</label>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxGROW|wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="ID_STATICTEXT3">
              <label>Methods</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxChoice" name="IDC_RATE_OPERATOR">
              <content/>
            </object>
          </object>
        </object>
      </object>
      <object class="spacer">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
      </object>
      <object class="spacer">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <object class="wxBoxSizer">
              <orient>wxHORIZONTAL</orient>
              <object class="sizeritem">
                <object class="wxStaticText" name="ID_STATICTEXT4">
                  <label>Weights files</label>
                </object>
                <flag>wxALIGN_CENTRE_VERTICAL</flag>
              </object>
              <object class="spacer">
                <size>5,5d</size>
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>2</border>
              </object>
              <object class="sizeritem">
                <object class="wxBitmapButton" name="ID_OPEN_WEIGHT">
                  <bitmap stock_id="ToolBarBitmaps_3"/>
                  <disabled stock_id="ToolBarBitmaps_3_disabled"/>
                  <tooltip>Open weights file</tooltip>
                </object>
                <flag>wxALIGN_CENTRE_VERTICAL</flag>
              </object>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxGROW|wxALL</flag>
            <border>5</border>
            <object class="wxChoice" name="IDC_RATE_WEIGHT">
              <content/>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxFlexGridSizer">
              <cols>2</cols>
              <rows>2</rows>
              <vgap>0</vgap>
              <hgap>0</hgap>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="IDC_STATIC">
                  <label>Event Variables</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="ID_STATICTEXT5">
                  <label>Base Variables</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxChoice" name="IDC_RATE_OPERAND1">
                  <content/>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxChoice" name="IDC_RATE_OPERAND2">
                  <content/>
                </object>
              </object>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_SAVE_RATES" subclass="CSaveRateDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Save Rates</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_LEFT|wxALL|wxADJUST_MINSIZE</flag>
        <border>5</border>
        <object class="wxStaticText" name="wxID_TITLE">
          <label>title</label>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_LEFT|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxHORIZONTAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxVERTICAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="IDC_STATIC">
                  <label>Suggested column name:</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALL</flag>
                <border>5</border>
                <object class="wxComboBox" name="IDC_COMBO1">
                  <content/>
                  <style>wxCB_DROPDOWN</style>
                </object>
              </object>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxVERTICAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                <border>5</border>
                <object class="wxButton" name="wxID_OK">
                  <label>OK</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                <border>5</border>
                <object class="wxButton" name="wxID_CANCEL">
                  <label>Close</label>
                </object>
              </object>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_SAVE_SELECTION" subclass="CSaveSelectionDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Save Selected To Column</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxHORIZONTAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="IDC_STATIC">
              <label>Suggested Column Name</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxComboBox" name="IDC_FIELD2">
              <content/>
              <style>wxCB_DROPDOWN</style>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDOK">
              <label>&amp;OK</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>&amp;Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_SAVE_MORAN" subclass="CSaveMoranIDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Save Moran-Plot Results</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxHORIZONTAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxCheckBox" name="IDC_CHECK1">
              <style>wxCHK_2STATE</style>
              <label>Standardized Data:</label>
              <checked>0</checked>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxCheckBox" name="IDC_CHECK2">
              <style>wxCHK_2STATE</style>
              <label>Spatial Lag:</label>
              <checked>0</checked>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxComboBox" name="IDC_COMBO1">
              <content/>
              <style>wxCB_DROPDOWN</style>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxComboBox" name="IDC_COMBO2">
              <content/>
              <style>wxCB_DROPDOWN</style>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDOK">
              <label>OK</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_SAVE_CENTROIDS" subclass="CSaveCentroidsDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Add Centroids to Table</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxHORIZONTAL</orient>
      <object class="sizeritem">
        <object class="wxFlexGridSizer">
          <object class="sizeritem">
            <object class="wxCheckBox" name="IDC_CHECK1">
              <label>X-Coordinates</label>
            </object>
            <flag>wxALIGN_CENTRE_VERTICAL</flag>
          </object>
          <object class="sizeritem">
            <object class="wxComboBox" name="IDC_COMBO1">
              <content/>
              <size>90,16d</size>
              <style>wxCB_DROPDOWN</style>
            </object>
          </object>
          <object class="sizeritem">
            <object class="wxCheckBox" name="IDC_CHECK2">
              <label>Y-Coordinates</label>
            </object>
            <flag>wxALIGN_CENTRE_VERTICAL</flag>
          </object>
          <object class="sizeritem">
            <object class="wxComboBox" name="IDC_COMBO2">
              <content/>
              <size>90,16d</size>
              <style>wxCB_DROPDOWN</style>
            </object>
            <flag>wxALIGN_CENTRE_VERTICAL</flag>
          </object>
          <cols>2</cols>
          <rows>2</rows>
          <vgap>3</vgap>
          <hgap>5</hgap>
        </object>
        <flag>wxALL|wxALIGN_CENTRE_VERTICAL</flag>
        <border>7</border>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <object class="wxButton" name="wxID_OK">
              <label>OK</label>
            </object>
            <option>1</option>
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxPanel" name="IDD_MAPMOVIE" subclass="CMovieControlPan">
    <object class="wxBoxSizer">
      <orient>wxHORIZONTAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxHORIZONTAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxButton" name="IDC_BUTTON1">
                  <label>Reset</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxButton" name="IDC_BUTTON2">
                  <label>Pause</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxButton" name="IDC_BUTTON3">
                  <label>&lt;&lt;</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxButton" name="IDC_BUTTON4">
                  <label>Play</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxButton" name="IDC_BUTTON5">
                  <label>&gt;&gt;</label>
                </object>
              </object>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_RIGHT|wxALL</flag>
            <border>5</border>
            <object class="wxCheckBox" name="ID_CHECKBOX1">
              <style>wxCHK_2STATE</style>
              <label>Reverse</label>
              <checked>0</checked>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="IDC_STATIC">
              <label>Speed Control (ms)</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxSlider" name="IDC_SLIDER1">
              <size>91,-1d</size>
              <style>wxSL_HORIZONTAL</style>
              <value>70</value>
              <min>1</min>
              <max>300</max>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
        <border>5</border>
        <object class="wxStaticText" name="IDC_STATIC1">
          <size>30,-1d</size>
          <label>700</label>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_PCP" subclass="CPCPDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Parallel Coordinate Plot</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxHORIZONTAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxVERTICAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="ID_STATICTEXT">
                  <label>Do not include</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                <border>5</border>
                <object class="wxListBox" name="IDC_LIST_VARIN">
                  <content/>
                  <size>90,107d</size>
                  <style>wxLB_SINGLE</style>
                </object>
              </object>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxVERTICAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                <border>5</border>
                <object class="wxButton" name="IDC_MOVEOUT_ALL">
                  <label>&gt;&gt;</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                <border>5</border>
                <object class="wxButton" name="IDC_MOVEOUT_ONE">
                  <label>&gt;</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                <border>5</border>
                <object class="wxButton" name="IDC_MOVEIN_ONE">
                  <label>&lt;</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                <border>5</border>
                <object class="wxButton" name="IDC_MOVEIN_ALL">
                  <label>&lt;&lt;</label>
                </object>
              </object>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxVERTICAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="IDC_STATIC">
                  <label>Include</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                <border>5</border>
                <object class="wxListBox" name="IDC_LIST_VAROUT">
                  <content/>
                  <size>90,107d</size>
                  <style>wxLB_SINGLE</style>
                </object>
              </object>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxHORIZONTAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_OK">
              <label>OK</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_VARIOGRAM_2DPAIR" subclass="CVariog2DPairDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <exstyle>wxWS_EX_BLOCK_EVENTS</exstyle>
    <title>Variogram Settings</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxRadioButton" name="IDC_RADIO4">
              <label>Open existing file of 2D pair distances</label>
              <style>wxRB_GROUP</style>
              <value>0</value>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxHORIZONTAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_EDIT1">
                  <size>190,-1d</size>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBitmapButton" name="IDC_OPEN_FILEWEIGHT">
                  <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
                  <bitmap stock_id="open-folder"/>
                </object>
              </object>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxRadioButton" name="IDC_RADIO5">
              <label>Create 2D pair distances</label>
              <value>0</value>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxStaticBoxSizer" name="wxID_ANY">
              <orient>wxVERTICAL</orient>
              <label>Specify the XY-coordinates</label>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                <border>5</border>
                <object class="wxBoxSizer">
                  <orient>wxVERTICAL</orient>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxFlexGridSizer">
                      <cols>2</cols>
                      <rows>2</rows>
                      <vgap>0</vgap>
                      <hgap>0</hgap>
                      <object class="sizeritem">
                        <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                        <border>5</border>
                        <object class="wxStaticText" name="IDC_STATIC1">
                          <label>X-coordinates</label>
                        </object>
                      </object>
                      <object class="sizeritem">
                        <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                        <border>5</border>
                        <object class="wxStaticText" name="IDC_STATIC2">
                          <label>Y-coordinates</label>
                        </object>
                      </object>
                      <object class="sizeritem">
                        <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                        <border>5</border>
                        <object class="wxComboBox" name="IDC_XCOORDINATES">
                          <content/>
                          <size>98,-1d</size>
                          <style>wxCB_DROPDOWN</style>
                        </object>
                      </object>
                      <object class="sizeritem">
                        <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                        <border>5</border>
                        <object class="wxComboBox" name="IDC_YCOORDINATES">
                          <content/>
                          <size>98,-1d</size>
                          <style>wxCB_DROPDOWN</style>
                        </object>
                      </object>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_LEFT|wxALL</flag>
                    <border>5</border>
                    <object class="wxStaticBoxSizer" name="wxID_ANY">
                      <orient>wxHORIZONTAL</orient>
                      <label>Methods for computing distances</label>
                      <object class="sizeritem">
                        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                        <border>5</border>
                        <object class="wxRadioButton" name="IDC_RADIO1">
                          <label>Euclidean distance</label>
                          <value>0</value>
                        </object>
                      </object>
                      <object class="sizeritem">
                        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                        <border>5</border>
                        <object class="wxRadioButton" name="IDC_RADIO2">
                          <label>Arc Distance (in miles)</label>
                          <value>0</value>
                        </object>
                      </object>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_LEFT|wxALL</flag>
                    <border>5</border>
                    <object class="wxBoxSizer">
                      <orient>wxHORIZONTAL</orient>
                      <object class="sizeritem">
                        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                        <border>5</border>
                        <object class="wxButton" name="IDC_BUTTON2">
                          <label>Comptute</label>
                        </object>
                      </object>
                      <object class="spacer">
                        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                        <border>5</border>
                        <size>5,5d</size>
                      </object>
                      <object class="spacer">
                        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                        <border>5</border>
                        <size>5,5d</size>
                      </object>
                      <object class="spacer">
                        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                        <border>5</border>
                        <size>5,5d</size>
                      </object>
                      <object class="sizeritem">
                        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                        <border>5</border>
                        <object class="wxButton" name="IDC_BUTTON1">
                          <label>Save 2D Pair</label>
                        </object>
                      </object>
                    </object>
                  </object>
                </object>
              </object>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_LEFT|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="IDC_STATIC">
              <label>Variable</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxComboBox" name="IDC_IDVARIABLE">
              <content/>
              <size>98,-1d</size>
              <style>wxCB_DROPDOWN</style>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxHORIZONTAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDOK">
              <label>OK</label>
            </object>
          </object>
          <object class="spacer">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <size>5,5d</size>
          </object>
          <object class="spacer">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <size>5,5d</size>
          </object>
          <object class="spacer">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <size>5,5d</size>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDCANCEL">
              <label>Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_REGRESSION" subclass="CRegressionDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Regression</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxFlexGridSizer">
          <cols>2</cols>
          <rows>2</rows>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="ID_STATICTEXT2">
              <label>Select Variables</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="ID_STATICTEXT">
              <label>Dependent Variable</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxListBox" name="IDC_LIST_VARIN">
              <content/>
              <size>90,114d</size>
              <style>wxLB_SINGLE</style>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxFlexGridSizer">
              <cols>2</cols>
              <rows>4</rows>
              <vgap>0</vgap>
              <hgap>0</hgap>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxButton" name="IDC_BUTTON1">
                  <label>&gt;</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_DEPENDENT_VAR">
                  <size>90,-1d</size>
                </object>
              </object>
              <object class="spacer">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <size>5,5d</size>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="ID_STATICTEXT1">
                  <label>Independent Variables</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBoxSizer">
                  <orient>wxVERTICAL</orient>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxButton" name="IDC_BUTTON2">
                      <label>&gt;</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxButton" name="IDC_BUTTON4">
                      <label>&gt;&gt;</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxButton" name="IDC_BUTTON3">
                      <label>&lt;</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxButton" name="IDC_BUTTON5">
                      <label>&lt;&lt;</label>
                    </object>
                  </object>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxListBox" name="IDC_LIST_VAROUT">
                  <content/>
                  <size>90,85d</size>
                  <style>wxLB_SINGLE</style>
                </object>
              </object>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <object class="wxBoxSizer">
          <object class="sizeritem">
            <object class="wxCheckBox" name="IDC_WEIGHT_CHECK">
              <label>Weights File</label>
            </object>
            <flag>wxALL|wxALIGN_LEFT|wxALIGN_CENTRE_VERTICAL</flag>
            <border>5</border>
          </object>
          <object class="sizeritem">
            <object class="wxChoice" name="IDC_CURRENTUSED_W">
              <content/>
              <size>162,-1d</size>
            </object>
            <flag>wxALL|wxALIGN_CENTRE|wxALIGN_CENTRE_VERTICAL</flag>
            <border>5</border>
          </object>
          <object class="sizeritem">
            <object class="wxBitmapButton" name="ID_OPEN_WEIGHT">
              <bitmap stock_id="ToolBarBitmaps_3"/>
              <disabled stock_id="ToolBarBitmaps_3_disabled"/>
              <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
            </object>
            <flag>wxALL|wxALIGN_RIGHT|wxALIGN_CENTRE_VERTICAL</flag>
            <border>5</border>
          </object>
          <orient>wxHORIZONTAL</orient>
        </object>
        <flag>wxALL|wxALIGN_CENTRE_HORIZONTAL</flag>
        <border>5</border>
      </object>
      <object class="sizeritem">
        <flag>wxALL|wxALIGN_CENTRE_HORIZONTAL</flag>
        <object class="wxStaticBoxSizer" name="wxID_ANY">
          <orient>wxVERTICAL</orient>
          <label>Models</label>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <object class="wxBoxSizer">
              <orient>wxVERTICAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                <border>5</border>
                <object class="wxBoxSizer">
                  <orient>wxHORIZONTAL</orient>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxRadioButton" name="IDC_RADIO1">
                      <label>Classic </label>
                      <style>wxRB_GROUP</style>
                      <value>0</value>
                    </object>
                  </object>
                  <object class="spacer">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                    <size>5,5d</size>
                  </object>
                  <object class="spacer">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                    <size>5,5d</size>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxRadioButton" name="IDC_RADIO2">
                      <label>Spatial Lag</label>
                      <value>0</value>
                    </object>
                  </object>
                  <object class="spacer">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                    <size>5,5d</size>
                  </object>
                  <object class="spacer">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                    <size>5,5d</size>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxRadioButton" name="IDC_RADIO3">
                      <label>Spatial Error</label>
                      <value>0</value>
                    </object>
                  </object>
                </object>
              </object>
              <object class="sizeritem">
                <object class="wxBoxSizer">
                  <object class="spacer">
                    <size>5,5d</size>
                    <border>0</border>
                  </object>
                  <object class="sizeritem">
                    <object class="wxGauge" name="IDC_GAUGE">
                      <size>125,16d</size>
                      <range>125</range>
                      <value>0</value>
                    </object>
                    <flag>wxALL|wxALIGN_LEFT</flag>
                    <border>0</border>
                  </object>
                  <object class="spacer">
                    <size>15,5d</size>
                    <border>0</border>
                  </object>
                  <object class="sizeritem">
                    <object class="wxStaticText" name="IDC_GAUGE_TEXT">
                      <label>Progress</label>
                    </object>
                    <flag>wxALL|wxALIGN_RIGHT</flag>
                    <border>0</border>
                  </object>
                  <orient>wxHORIZONTAL</orient>
                </object>
              </object>
              <object class="sizeritem">
                <object class="wxBoxSizer">
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxButton" name="ID_RUN">
                      <label>&amp;Run</label>
                    </object>
                  </object>
                  <object class="spacer">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                    <size>5,5d</size>
                  </object>
                  <object class="spacer">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                    <size>5,5d</size>
                  </object>
                  <object class="spacer">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                    <size>5,5d</size>
                  </object>
                  <object class="spacer">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                    <size>5,5d</size>
                  </object>
                  <object class="spacer">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                    <size>5,5d</size>
                  </object>
                  <object class="sizeritem">
                    <object class="wxButton" name="IDC_SAVE_REGRESSION">
                      <label>&amp;Save to Table</label>
                    </object>
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                  </object>
                  <orient>wxHORIZONTAL</orient>
                </object>
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
              </object>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <object class="wxBoxSizer">
          <orient>wxHORIZONTAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDCANCEL">
              <size>50,14d</size>
              <pos>10,278d</pos>
              <label>&amp;Close</label>
            </object>
          </object>
          <object class="spacer">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <size>5,5d</size>
          </object>
          <object class="spacer">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <size>5,5d</size>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDC_RESET">
              <size>50,14d</size>
              <pos>87,278d</pos>
              <label>Re&amp;set</label>
            </object>
          </object>
          <object class="spacer">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <size>5,5d</size>
          </object>
          <object class="spacer">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <size>5,5d</size>
          </object>
          <object class="sizeritem">
            <object class="wxButton" name="ID_VIEW_RESULTS">
              <pos>164,278d</pos>
              <size>50,14d</size>
              <label>View Results</label>
            </object>
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
          </object>
        </object>
        <border>2</border>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_SAVE_REGRESSIONS" subclass="CSaveRegressionDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Save Regression Results</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxHORIZONTAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxStaticBoxSizer" name="wxID_ANY">
          <orient>wxHORIZONTAL</orient>
          <label>Results</label>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxFlexGridSizer">
              <cols>2</cols>
              <rows>4</rows>
              <vgap>0</vgap>
              <hgap>0</hgap>
              <object class="spacer">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <size>5,5d</size>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="IDC_STATIC">
                  <label>Suggested Name</label>
                </object>
              </object>
              <object class="sizeritem">
                <object class="wxCheckBox" name="IDC_CHECK_PRED_VAL">
                  <size>70,-1d</size>
                  <label>Predicted Value</label>
                </object>
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
              </object>
              <object class="sizeritem">
                <object class="wxComboBox" name="IDC_COMBO_PRED_VAL">
                  <content/>
                  <size>90,-1d</size>
                  <style>wxCB_DROPDOWN</style>
                </object>
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
              </object>
              <object class="sizeritem">
                <object class="wxCheckBox" name="IDC_CHECK_PRED_ERR">
                  <size>70,-1d</size>
                  <label>Prediction Error</label>
                </object>
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
              </object>
              <object class="sizeritem">
                <object class="wxComboBox" name="IDC_COMBO_PRED_ERR">
                  <content/>
                  <size>90,-1d</size>
                  <style>wxCB_DROPDOWN</style>
                </object>
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
              </object>
              <object class="sizeritem">
                <object class="wxCheckBox" name="IDC_CHECK_RESID">
                  <size>70,-1d</size>
                  <label>Residual</label>
                </object>
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
              </object>
              <object class="sizeritem">
                <object class="wxComboBox" name="IDC_COMBO_RESID">
                  <content/>
                  <size>90,-1d</size>
                  <style>wxCB_DROPDOWN</style>
                </object>
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
              </object>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_OK">
              <label>OK</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_REGRESSION_SAVE" subclass="CRegressionTitleDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Regression Title and Output</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_LEFT|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="ID_STATICTEXT">
              <label>Report Title</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxTextCtrl" name="IDC_EDIT1">
              <size>205,-1d</size>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_LEFT|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="ID_STATICTEXT1">
              <label>Output file name</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxHORIZONTAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_TOP|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_EDIT2">
                  <size>115,-1d</size>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_TOP|wxALL</flag>
                <border>5</border>
                <object class="wxBitmapButton" name="ID_BROWSE">
                  <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
                  <bitmap stock_id="save"/>
                </object>
              </object>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_LEFT|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="IDC_STATIC">
              <label>Information in the output includes:</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_RIGHT|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxHORIZONTAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBoxSizer">
                  <orient>wxVERTICAL</orient>
                  <object class="sizeritem">
                    <flag>wxALIGN_LEFT|wxALL</flag>
                    <border>5</border>
                    <object class="wxCheckBox" name="IDC_CHECK1">
                      <style>wxCHK_2STATE</style>
                      <label>Predicted Value and Residual</label>
                      <checked>0</checked>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_LEFT|wxALL</flag>
                    <border>5</border>
                    <object class="wxCheckBox" name="IDC_CHECK2">
                      <style>wxCHK_2STATE</style>
                      <label>Coefficient Variance Matrix</label>
                      <checked>0</checked>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_LEFT|wxALL</flag>
                    <border>5</border>
                    <object class="wxCheckBox" name="IDC_CHECK3">
                      <style>wxCHK_2STATE</style>
                      <label>Moran's I  z-value</label>
                      <checked>0</checked>
                    </object>
                  </object>
                </object>
              </object>
              <object class="spacer">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <size>5,5d</size>
              </object>
              <object class="spacer">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <size>5,5d</size>
              </object>
              <object class="spacer">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <size>5,5d</size>
              </object>
              <object class="spacer">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <size>5,5d</size>
              </object>
              <object class="spacer">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <size>5,5d</size>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBoxSizer">
                  <orient>wxVERTICAL</orient>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxButton" name="wxID_OK">
                      <label>OK</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxButton" name="wxID_CANCEL">
                      <label>Close</label>
                    </object>
                  </object>
                </object>
              </object>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_REGRESSION_REPORT" subclass="CRegressionReportDlg">
    <object class="wxGridSizer">
      <cols>1</cols>
      <rows>1</rows>
      <vgap>5</vgap>
      <hgap>5</hgap>
      <object class="sizeritem">
        <object class="wxTextCtrl" name="ID_TEXTCTRL1">
          <pos>0,0</pos>
          <size>620,560</size>
          <font>
            <size>10</size>
            <style>normal</style>
            <weight>normal</weight>
            <underlined>0</underlined>
            <family>default</family>
            <face>Courier</face>
          </font>
          <style>wxTE_MULTILINE|wxTE_READONLY</style>
        </object>
        <option>1</option>
        <flag>wxEXPAND|wxALIGN_CENTRE</flag>
      </object>
    </object>
    <size>620,560</size>
    <title>Regression Report</title>
    <centered>1</centered>
    <style>wxCAPTION|wxSYSTEM_MENU|wxRESIZE_BORDER|wxCLOSE_BOX</style>
  </object>
  <object class="wxDialog" name="IDD_CONDITION_VIEW_SETTING" subclass="CConditionViewDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Choose View Type</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxHORIZONTAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxRadioButton" name="IDC_RADIO1">
              <label>Map View</label>
              <value>1</value>
              <style>wxRB_GROUP</style>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxRadioButton" name="IDC_RADIO2">
              <label>Box Plot</label>
              <value>0</value>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxRadioButton" name="IDC_RADIO3">
              <label>Histogram</label>
              <value>0</value>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxRadioButton" name="IDC_RADIO4">
              <label>Scatter Plot</label>
              <value>0</value>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_TOP|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_OK">
              <label>OK</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_GET_DBF" subclass="CGetDbfFileDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Get DBF File</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxHORIZONTAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="IDC_STATIC">
              <label>Input file name (*.dbf)</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxHORIZONTAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBitmapButton" name="IDC_INPUTFILE">
                  <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
                  <bitmap stock_id="open-folder"/>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_EDIT_DBF">
                  <size>95,-1d</size>
                </object>
              </object>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_OK">
              <label>OK</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_CREATE_GRID" subclass="">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Creating Grid</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxStaticBoxSizer" name="wxID_ANY">
          <orient>wxVERTICAL</orient>
          <label>Grid Bounding Box</label>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxVERTICAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALL</flag>
                <border>5</border>
                <object class="wxRadioButton" name="IDC_RADIO1">
                  <label>Specify manually</label>
                  <style>wxRB_GROUP</style>
                  <value>1</value>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                <border>5</border>
                <object class="wxFlexGridSizer">
                  <cols>3</cols>
                  <rows>3</rows>
                  <vgap>0</vgap>
                  <hgap>0</hgap>
                  <object class="spacer">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                    <size>5,5d</size>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                    <border>5</border>
                    <object class="wxStaticText" name="ID_STATICTEXT3">
                      <label>X-coordinate</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                    <border>5</border>
                    <object class="wxStaticText" name="ID_STATICTEXT2">
                      <label>Y-coordinate</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                    <border>5</border>
                    <object class="wxStaticText" name="ID_STATICTEXT1">
                      <label>Lower-left corner</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxTextCtrl" name="IDC_EDIT1">
                      <style>wxTE_RIGHT</style>
                      <value>0.0</value>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxTextCtrl" name="IDC_EDIT2">
                      <style>wxTE_RIGHT</style>
                      <value>0.0</value>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                    <border>5</border>
                    <object class="wxStaticText" name="ID_STATICTEXT">
                      <label>Upper-right corner</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxTextCtrl" name="IDC_EDIT3">
                      <style>wxTE_RIGHT</style>
                      <value>0.0</value>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxTextCtrl" name="IDC_EDIT4">
                      <style>wxTE_RIGHT</style>
                      <value>0.0</value>
                    </object>
                  </object>
                </object>
              </object>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxVERTICAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALL</flag>
                <border>5</border>
                <object class="wxRadioButton" name="IDC_RADIO3">
                  <label>Use the bounding box of a shape file</label>
                  <value>0</value>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                <border>5</border>
                <object class="wxBoxSizer">
                  <orient>wxHORIZONTAL</orient>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxTextCtrl" name="IDC_EDIT5">
                      <size>179,-1d</size>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                    <object class="wxBitmapButton" name="IDC_REFERENCEFILE2">
                      <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
                      <bitmap stock_id="open-folder"/>
                    </object>
                  </object>
                </object>
              </object>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_LEFT|wxALL</flag>
        <border>5</border>
        <object class="wxStaticBoxSizer" name="wxID_ANY">
          <orient>wxVERTICAL</orient>
          <label>Grid Size</label>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxFlexGridSizer">
              <cols>2</cols>
              <rows>2</rows>
              <vgap>0</vgap>
              <hgap>0</hgap>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="ID_STATICTEXT6">
                  <label>Number of Rows</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_EDIT7">
                  <style>wxTE_RIGHT</style>
                  <value>2</value>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="ID_STATICTEXT5">
                  <label>Number of Columns</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_EDIT8">
                  <style>wxTE_RIGHT</style>
                  <value>2</value>
                </object>
              </object>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="IDC_STATIC">
              <label>Save as (*.shp)</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxHORIZONTAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_EDIT9">
                  <size>199,-1d</size>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBitmapButton" name="IDC_BROWSE_OFILE">
                  <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
                  <bitmap stock_id="ToolBar_export"/>
                </object>
              </object>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxHORIZONTAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="ID_CREATE">
              <label>C&amp;reate</label>
            </object>
          </object>
          <object class="spacer">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <size>5,5d</size>
          </object>
          <object class="spacer">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <size>5,5d</size>
          </object>
          <object class="spacer">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <size>5,5d</size>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDCANCEL">
              <label>&amp;Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_CONVERT_BOUNDARY_TO_SHP" subclass="CBnd2ShpDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Convert Boundary to SHP</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxStaticBoxSizer" name="wxID_ANY">
          <orient>wxHORIZONTAL</orient>
          <label/>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxFlexGridSizer">
              <cols>3</cols>
              <rows>2</rows>
              <vgap>0</vgap>
              <hgap>0</hgap>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="IDC_STATIC">
                  <label>Input file (text file)</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_FIELD_ASC">
                  <size>172,-1d</size>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBitmapButton" name="IDC_OPEN_IASC">
                  <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
                  <bitmap stock_id="open-folder"/>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="ID_STATICTEXT">
                  <label>Output file (*.shp)</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_FIELD_SHP">
                  <size>172,-1d</size>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBitmapButton" name="IDC_OPEN_OSHP">
                  <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
                  <bitmap stock_id="save"/>
                </object>
              </object>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxHORIZONTAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="ID_CREATE">
              <label>C&amp;reate</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDCANCEL">
              <label>&amp;Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_3DPLOT" subclass="C3DDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Axis Selection</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxHORIZONTAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxStaticBoxSizer" name="wxID_ANY">
              <orient>wxVERTICAL</orient>
              <label>X Variable</label>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                <border>5</border>
                <object class="wxListBox" name="IDC_LIST_VARIN_X">
                  <content/>
                  <size>90,107d</size>
                  <style>wxLB_SINGLE</style>
                </object>
              </object>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxStaticBoxSizer" name="wxID_ANY">
              <orient>wxVERTICAL</orient>
              <label>Y Variable</label>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                <border>5</border>
                <object class="wxListBox" name="IDC_LIST_VARIN_Y">
                  <content/>
                  <size>90,107d</size>
                  <style>wxLB_SINGLE</style>
                </object>
              </object>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxStaticBoxSizer" name="wxID_ANY">
              <orient>wxVERTICAL</orient>
              <label>Z Variable</label>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
                <border>5</border>
                <object class="wxListBox" name="IDC_LIST_VARIN_Z">
                  <content/>
                  <size>90,107d</size>
                  <style>wxLB_SINGLE</style>
                </object>
              </object>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxHORIZONTAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_OK">
              <label>OK</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxPanel" name="IDD_3DCONTROL" subclass="C3DControlPan">
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_LEFT|wxALL</flag>
        <border>5</border>
        <object class="wxStaticBoxSizer" name="wxID_ANY">
          <orient>wxVERTICAL</orient>
          <label>View</label>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxCheckBox" name="IDC_DATAPOINT">
              <style>wxCHK_2STATE</style>
              <label>Data Point</label>
              <checked>1</checked>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxCheckBox" name="IDC_TOX">
              <style>wxCHK_2STATE</style>
              <label>Project to Z-Y</label>
              <checked>0</checked>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALL</flag>
            <border>5</border>
            <object class="wxCheckBox" name="IDC_TOY">
              <style>wxCHK_2STATE</style>
              <label>Project to X-Z</label>
              <checked>0</checked>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxCheckBox" name="IDC_TOZ">
              <style>wxCHK_2STATE</style>
              <label>Project to X-Y</label>
              <checked>0</checked>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_LEFT|wxALL</flag>
        <border>5</border>
        <object class="wxCheckBox" name="IDC_SELECT">
          <style>wxCHK_2STATE</style>
          <label>Select, hold CTRL for brushing</label>
          <checked>0</checked>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxFlexGridSizer">
          <cols>2</cols>
          <rows>6</rows>
          <vgap>0</vgap>
          <hgap>0</hgap>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALIGN_TOP|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="ID_3D_STATICTEXT_X">
              <label>X</label>
            </object>
          </object>
          <object class="spacer">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <size>5,5d</size>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_TOP|wxALL</flag>
            <border>5</border>
            <object class="wxSlider" name="IDC_SLXP">
              <size>56,-1d</size>
              <style>wxSL_HORIZONTAL</style>
              <value>0</value>
              <min>0</min>
              <max>100</max>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_TOP|wxALL</flag>
            <border>5</border>
            <object class="wxSlider" name="IDC_SLXS">
              <size>56,-1d</size>
              <style>wxSL_HORIZONTAL</style>
              <value>0</value>
              <min>0</min>
              <max>100</max>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="ID_3D_STATICTEXT_Y">
              <label>Y</label>
            </object>
          </object>
          <object class="spacer">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <size>5,5d</size>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxSlider" name="IDC_SLYP">
              <size>56,-1d</size>
              <style>wxSL_HORIZONTAL</style>
              <value>0</value>
              <min>0</min>
              <max>100</max>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxSlider" name="IDC_SLYS">
              <size>56,-1d</size>
              <style>wxSL_HORIZONTAL</style>
              <value>0</value>
              <min>0</min>
              <max>100</max>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALIGN_BOTTOM|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="ID_3D_STATICTEXT_Z">
              <label>Z</label>
            </object>
          </object>
          <object class="spacer">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <size>5,5d</size>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_BOTTOM|wxALL</flag>
            <border>5</border>
            <object class="wxSlider" name="IDC_SLZP">
              <size>56,-1d</size>
              <style>wxSL_HORIZONTAL</style>
              <value>0</value>
              <min>0</min>
              <max>100</max>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_BOTTOM|wxALL</flag>
            <border>5</border>
            <object class="wxSlider" name="IDC_SLZS">
              <size>56,-1d</size>
              <style>wxSL_HORIZONTAL</style>
              <value>0</value>
              <min>0</min>
              <max>100</max>
            </object>
          </object>
        </object>
        <object class="sizeritem">
          <flag>wxALIGN_LEFT|wxALIGN_TOP|wxALL|wxADJUST_MINSIZE</flag>
          <border>5</border>
          <object class="wxStaticText" name="ID_STATICTEXT2">
            <label>Zoom : press right-mouse button</label>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_CC_VARIABLES" subclass="CCCVariableDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Conditional Plot Variable Settings</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxHORIZONTAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxListBox" name="IDC_LIST_VARIN">
              <content/>
              <size>90,107d</size>
              <style>wxLB_SINGLE</style>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxFlexGridSizer">
              <cols>3</cols>
              <rows>4</rows>
              <vgap>0</vgap>
              <hgap>0</hgap>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxButton" name="IDC_MOVEOUT_1">
                  <label>&gt;</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_EDIT1">
                  <size>78,-1d</size>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="IDC_STATIC">
                  <style>wxALIGN_RIGHT</style>
                  <label>X Variable</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxButton" name="IDC_MOVEOUT_2">
                  <label>&gt;</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_EDIT2">
                  <size>78,-1d</size>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="ID_STATICTEXT1">
                  <style>wxALIGN_RIGHT</style>
                  <label>Y variable</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxButton" name="IDC_MOVEOUT_3">
                  <label>&gt;</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_EDIT3">
                  <size>78,-1d</size>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="ID_STATICTEXT">
                  <style>wxALIGN_RIGHT</style>
                  <label>Variable 1</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxGROW|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxButton" name="IDC_MOVEOUT_4">
                  <label>&gt;</label>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_EDIT4">
                  <size>78,-1d</size>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="IDC_STATIC4">
                  <style>wxALIGN_RIGHT</style>
                  <label>Variable 2</label>
                </object>
              </object>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxHORIZONTAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_OK">
              <label>OK</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_FIELDCALC_SHEET" subclass="CFieldCalcSheetDlg">
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <object class="wxNotebook" name="ID_NOTEBOOK">
          <size>750,300</size>
        </object>
        <flag>wxALIGN_CENTRE_HORIZONTAL</flag>
      </object>
      <object class="sizeritem">
        <object class="wxBoxSizer">
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="ID_APPLY">
              <label>Apply</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxGROW|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>Close</label>
            </object>
          </object>
          <orient>wxHORIZONTAL</orient>
        </object>
        <flag>wxALIGN_CENTRE_HORIZONTAL</flag>
      </object>
    </object>
    <title>Field Calculation</title>
    <centered>1</centered>
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
  </object>
  <object class="wxDialog" name="IDD_USERCONFIG_DIALOG" subclass="CUserConfigDlg">
    <style>wxCAPTION|wxRESIZE_BORDER|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <size>400,300</size>
    <title>User Configure</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_LEFT|wxALL|wxADJUST_MINSIZE</flag>
        <border>5</border>
        <object class="wxStaticText" name="wxID_STATIC">
          <label/>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxHORIZONTAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxTextCtrl" name="ID_TEXTCTRL2"/>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="wxID_STATIC">
              <label>~</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxTextCtrl" name="ID_TEXTCTRL3"/>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxHORIZONTAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_OK">
              <label>&amp;OK</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>&amp;Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_INVERSEDISTANCE_DIALOG" subclass="CInverseDistanceDlg">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Inverse Distance</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxFlexGridSizer">
          <cols>3</cols>
          <rows>2</rows>
          <vgap>0</vgap>
          <hgap>0</hgap>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="ID_STATICTEXT1">
              <label>Input Distance File (*.gwt)</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxTextCtrl" name="ID_IN_SHP_TXT_CTRL">
              <size>149,-1</size>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxBitmapButton" name="IDC_BROWSE_ISHP4W">
              <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
              <bitmap stock_id="open-folder"/>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_LEFT|wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
            <object class="wxStaticText" name="ID_STATICTEXT">
              <label>Save output as</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxTextCtrl" name="IDC_EDIT_OSHP4W">
              <size>149,-1</size>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxBitmapButton" name="IDC_BROWSE_OSHP4W">
              <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
              <bitmap stock_id="save"/>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_RIGHT|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxBoxSizer">
              <orient>wxHORIZONTAL</orient>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                <border>5</border>
                <object class="wxStaticText" name="wxID_STATIC">
                  <label>Power</label>
                </object>
              </object>
              <object class="spacer">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <size>5,5</size>
              </object>
              <object class="spacer">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <size>5,5</size>
              </object>
              <object class="spacer">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <size>5,5</size>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="ID_TEXTCTRL4">
                  <style>wxTE_READONLY|wxTE_RIGHT</style>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxSpinButton" name="IDC_SPIN_POWER">
                  <style>wxSP_VERTICAL</style>
                  <value>0</value>
                  <min>0</min>
                  <max>200</max>
                </object>
              </object>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_RIGHT|wxALL</flag>
        <border>5</border>
        <object class="wxCheckBox" name="ID_STANDARDIZE">
          <style>wxCHK_2STATE</style>
          <label>Standardize</label>
          <checked>1</checked>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxHORIZONTAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDOK_CREATE1">
              <label>&amp;OK</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="IDCANCEL">
              <label>&amp;Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_DIALOG_BOX_HINGE">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Box Plot Map</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxHORIZONTAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxStaticBoxSizer" name="wxID_ANY">
          <orient>wxHORIZONTAL</orient>
          <label/>
          <object class="sizeritem">
            <object class="wxStaticText" name="IDC_STATIC">
              <label>Hinge value</label>
            </object>
            <flag>wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxTextCtrl" name="IDC_EDIT_HINGE">
              <size>30,-1</size>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_OK">
              <label>OK</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_DIALOG_JENKS_SAMPLE">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>Jenks Caspall Sample Map</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxHORIZONTAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxStaticBoxSizer" name="wxID_ANY">
          <orient>wxHORIZONTAL</orient>
          <label/>
          <object class="sizeritem">
            <object class="wxStaticText" name="IDC_STATIC">
              <label>Sample percent</label>
            </object>
            <flag>wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxTextCtrl" name="IDC_EDIT_PERCENT">
              <size>30,-1</size>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_OK">
              <label>OK</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_DIALOG_USER_DEFINED">
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
    <title>User Defined Map</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxHORIZONTAL</orient>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxStaticBoxSizer" name="wxID_ANY">
          <orient>wxHORIZONTAL</orient>
          <label/>
          <object class="sizeritem">
            <object class="wxStaticText" name="IDC_STATIC">
              <label>Bins</label>
            </object>
            <flag>wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
            <border>5</border>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
            <border>5</border>
            <object class="wxTextCtrl" name="IDC_EDIT_Bins">
              <size>100,-1</size>
            </object>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_OK">
              <label>OK</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>Close</label>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <object class="wxDialog" name="IDD_DIALOG_TIME_WEIGHTS">
    <title>Time Weights Configuration</title>
    <centered>1</centered>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <object class="wxRadioButton" name="IDC_RADIO_OPENWEIGHT">
              <label>Select from file (gal, gwt)</label>
              <value>1</value>
            </object>
            <flag>wxALL|wxALIGN_LEFT</flag>
            <border>5</border>
          </object>
          <object class="sizeritem">
            <object class="wxBoxSizer">
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxTextCtrl" name="IDC_EDIT_FILEWEIGHT">
                  <size>178,-1d</size>
                </object>
              </object>
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxBitmapButton" name="IDC_OPEN_FILEWEIGHT">
                  <style>wxBU_AUTODRAW|wxBU_EXACTFIT</style>
                  <bitmap stock_id="open-folder"/>
                </object>
              </object>
              <orient>wxHORIZONTAL</orient>
            </object>
            <flag>wxALIGN_LEFT|wxALL</flag>
          </object>
        </object>
        <flag>wxALIGN_LEFT|wxALL</flag>
        <border>5</border>
      </object>
      <object class="sizeritem">
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <object class="wxRadioButton" name="IDC_RADIO_CREATEWEIGHT">
              <label>Create a Time Weights file</label>
            </object>
            <flag>wxALL|wxALIGN_LEFT</flag>
            <border>5</border>
          </object>
          
          <object class="sizeritem">
            <object class="wxBoxSizer">
              <object class="sizeritem">
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
                <object class="wxStaticBoxSizer" name="wxID_ANY">
                  <orient>wxHORIZONTAL</orient>
                  <label/>
                  <object class="sizeritem">
                    <object class="wxStaticText" name="IDC_STATIC_P_NEIGHBORS">
                      <label>Number of past time intervals as neighbors:</label>
                      <enabled>0</enabled>
                    </object>
                    <flag>wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                    <border>5</border>
                  </object>
                  <object class="sizeritem">
                    <object class="wxTextCtrl" name="IDC_EDIT_N_P_NEIGHBORS">
                      <size>100,-1</size>
                      <enabled>0</enabled>
                    </object>
                    <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                    <border>5</border>
                  </object>
                </object>
              </object>
              <orient>wxVERTICAL</orient>
              <object class="sizeritem">
                <object class="wxStaticBoxSizer" name="wxID_ANY">
                  <orient>wxHORIZONTAL</orient>
                  <label/>
                  <object class="sizeritem">
                    <object class="wxBoxSizer">
                      <orient>wxVERTICAL</orient>
                      <!--
                      <object class="sizeritem">
                        <object class="wxCheckBox" name="IDC_CHK_FUTURE">
                          <label>Consider Future Neighbors in Weights?</label>
                          <enabled>0</enabled>
                        </object>
                      </object>
                      -->
                      <object class="sizeritem">
                        <object class="wxBoxSizer">
                          <orient>wxHORIZONTAL</orient>
                          <object class="sizeritem">
                            <object class="wxStaticText" name="IDC_STATIC_F_NEIGHBORS">
                              <label>Number of future time intervals as neighbors:</label>
                              <enabled>0</enabled>
                            </object>
                            <flag>wxALIGN_CENTER_VERTICAL|wxALL|wxADJUST_MINSIZE</flag>
                            <border>5</border>
                          </object>
                          <object class="sizeritem">
                            <object class="wxTextCtrl" name="IDC_EDIT_N_F_NEIGHBORS">
                              <size>100,-1</size>
                              <enabled>0</enabled>
                            </object>
                            <flag>wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL|wxALL</flag>
                            <border>5</border>
                          </object>
                        </object>
                      </object>
                    </object>
                  </object>
                </object>
                <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
                <border>5</border>
              </object>
            </object>
          </object>
        </object>
        <flag>wxALIGN_LEFT|wxALL</flag>
        <border>5</border>
      </object>
      <object class="sizeritem">
        <object class="wxBoxSizer">
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_OK">
              <label>OK</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>Close</label>
            </object>
          </object>
          <orient>wxHORIZONTAL</orient>
        </object>
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
      </object>
    </object>
  </object>
  

  <object class="wxDialog" name="IDD_DIALOG_LOCAL_G">
    <object class="wxBoxSizer">
      <object class="sizeritem">
        <object class="wxBoxSizer" name="wxID_ANY">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <object class="wxStaticBoxSizer">
              <object class="sizeritem">
                <object class="wxRadioButton" name="IDC_RDO_GI">
                  <label>Gi map</label>
                  <style>wxRB_GROUP</style>
                </object>
              </object>
              <object class="sizeritem">
                <object class="wxRadioButton" name="IDC_RDO_GI_STAR">
                  <label>Gi* map</label>
                  <value>1</value>
                </object>
              </object>
              <label>Map type:</label>
              <orient>wxHORIZONTAL</orient>
            </object>
          </object>
          <object class="spacer">
            <size>0,10</size>
          </object>
          <object class="sizeritem">
            <object class="wxStaticBoxSizer">
              <object class="sizeritem">
                <object class="wxRadioButton" name="IDC_RDO_ROW_STAND">
                  <label>row-standardized</label>
                  <value>1</value>
                  <style>wxRB_GROUP</style>
                </object>
              </object>
              <object class="sizeritem">
                <object class="wxRadioButton" name="IDC_RDO_BINARY">
                  <label>binary</label>
                </object>
              </object>
              <label>Weights:</label>
              <orient>wxHORIZONTAL</orient>
            </object>
          </object>
        </object>
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
      </object>
      <object class="sizeritem">
        <object class="wxBoxSizer">
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_OK">
              <label>OK</label>
            </object>
          </object>
          <object class="sizeritem">
            <flag>wxALIGN_CENTER_HORIZONTAL|wxALL</flag>
            <border>5</border>
            <object class="wxButton" name="wxID_CANCEL">
              <label>Close</label>
            </object>
          </object>
          <orient>wxHORIZONTAL</orient>
        </object>
        <flag>wxALIGN_CENTER_VERTICAL|wxALL</flag>
        <border>5</border>
      </object>
      <orient>wxVERTICAL</orient>
    </object>
    <title>Local G Statistic Map</title>
    <centered>1</centered>
    <style>wxCAPTION|wxSYSTEM_MENU|wxCLOSE_BOX</style>
  </object>
</resource>
'''