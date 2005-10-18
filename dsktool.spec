Summary:	Diskette tools - GUI front-end to LibDsk
Summary(pl):	Narz�dzia do dyskietek - graficzny interfejs do LibDsk
Name:		dsktool
Version:	1.0.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://www.seasip.demon.co.uk/Unix/LibDsk/%{name}-%{version}.tar.gz
# Source0-md5:	d4468598b5ef1d588ad1797a67b748eb
URL:		http://www.seasip.demon.co.uk/Unix/LibDsk/#tools
BuildRequires:	libdsk-devel
BuildRequires:	rpmbuild(macros) >= 1.167
BuildRequires:	wxGTK2-devel >= 2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Diskette Tools program is a GUI front-end to LibDsk. It doesn't do
any more than the provided sample utilities, but it looks nicer.

%description -l pl
Program Diskette Tools to graficzny interfejs u�ytkownika do LibDsk.
Nie robi wi�cej ni� za��czone programy przyk�adowe, ale wygl�da
przyjemniej.

%prep
%setup -q

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags} `wx-gtk2-ansi-config --cflags`" \
	WX_LIBS="`wx-gtk2-ansi-config --libs`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	INSTALLDIR=$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_bindir}/dsktool