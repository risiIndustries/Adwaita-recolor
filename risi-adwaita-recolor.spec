Name:           risi-adwaita-recolor
Version:        0.1
Release:        1%{?dist}
Summary:        risiOS's accent colors for Adwaita

License:        GPL v3
URL:            risi.io
Source0:        https://github.com/risiOS/Adwaita-recolor/archive/refs/heads/main.tar.gz#/Adwaita-recolor-main.tar.gz

BuildArch:	noarch
Requires:	gtk
Requires:	gtk4
BuildRequires:	scss
BuildRequires:	inkscape
BuildRequires:	optipng

%description
This is a package with all of risiOS's Adwaita Varients

%prep
%autosetup -n %{gitname}-%{version}

%build
bash all-themes.sh

%install
# rm -rf $RPM_BUILD_ROOT

mkdir -p %{buildroot}%{_datadir}/themes
cp -R adwaita-brown %{buildroot}%{_datadir}/themes/
cp -R adwaita-green %{buildroot}%{_datadir}/themes/
cp -R adwaita-orange %{buildroot}%{_datadir}/themes/
cp -R adwaita-purple %{buildroot}%{_datadir}/themes/
cp -R adwaita-pink %{buildroot}%{_datadir}/themes/
cp -R adwaita-red %{buildroot}%{_datadir}/themes/
cp -R adwaita-brown-dark %{buildroot}%{_datadir}/themes/
cp -R adwaita-green-dark %{buildroot}%{_datadir}/themes/
cp -R adwaita-orange-dark %{buildroot}%{_datadir}/themes/
cp -R adwaita-purple-dark %{buildroot}%{_datadir}/themes/
cp -R adwaita-pink-dark %{buildroot}%{_datadir}/themes/
cp -R adwaita-red-dark %{buildroot}%{_datadir}/themes/

%files
# %license add-license-file-here
# %doc add-docs-here
%dir %{_datadir}/themes/adwaita-brown
%dir %{_datadir}/themes/adwaita-green
%dir %{_datadir}/themes/adwaita-orange
%dir %{_datadir}/themes/adwaita-purple
%dir %{_datadir}/themes/adwaita-pink
%dir %{_datadir}/themes/adwaita-red
%dir %{_datadir}/themes/adwaita-brown-dark
%dir %{_datadir}/themes/adwaita-green-dark
%dir %{_datadir}/themes/adwaita-orange-dark
%dir %{_datadir}/themes/adwaita-purple-dark
%dir %{_datadir}/themes/adwaita-pink-dark
%dir %{_datadir}/themes/adwaita-red-dark
	
%changelog
* Fri Sep 3 2021 PizzaLovingNerd
- First spec file
