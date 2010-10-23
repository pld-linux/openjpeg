%define fver    %(echo %{version} | tr . _)
Summary:	An open-source JPEG 2000 codec
Summary(pl.UTF-8):	Biblioteka kodująca i dekodująca format JPEG 2000
Name:		openjpeg
Version:	1.3
Release:	3
License:	BSD
Group:		Libraries
Source0:	http://openjpeg.googlecode.com/files/%{name}_v%{fver}.tar.gz
# Source0-md5:	f9a3ccfa91ac34b589e9bf7577ce8ff9
Patch0:		%{name}-install.patch
URL:		http://www.openjpeg.org/
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The OpenJPEG library is an open-source JPEG 2000 codec written in C
language. It has been developed in order to promote the use of JPEG
2000, the new still-image compression standard from the Joint
Photographic Experts Group (JPEG).

%description -l pl.UTF-8
OpenJPEG to mająca otwarte źródła biblioteka kodująca i dekodująca
format JPEG 2000, napisana w języku C. Powstała w celu promowania
użycia formatu JPEG 2000 - nowego standardu obrazów nieruchomych
stworzonego przez grupę JPEG (Joint Photographic Experts Group).

%package devel
Summary:	Header file for OpenJPEG library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki OpenJPEG
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header file needed for developing programs
using the OpenJPEG library.

%description devel -l pl.UTF-8
Ten pakiet zawiera plik nagłówkowy potrzebny do tworzenia programów
wykorzystujących bibliotekę OpenJPEG.

%package static
Summary:	Static OpenJPEG library
Summary(pl.UTF-8):	Statyczna biblioteka OpenJPEG
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static OpenJPEG library.

%description static -l pl.UTF-8
Statyczna biblioteka OpenJPEG.

%prep
%setup -q -n OpenJPEG_v%{fver}
%patch0 -p1

sed 's/$(CC) -s/$(CC) $(CFLAGS) $(LDFLAGS)/' -i Makefile
sed 's/-lstdc++/-lm/' -i Makefile

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -fPIC" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_LIBDIR=%{_libdir} \
	INSTALL_INCLUDE=%{_includedir}

cd $RPM_BUILD_ROOT%{_libdir}
ln -sf libopenjpeg.so.? libopenjpeg.so

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenjpeg-*.*.*.*.so
%attr(755,root,root) %ghost %{_libdir}/libopenjpeg.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenjpeg.so
%{_includedir}/%{name}.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libopenjpeg.a
