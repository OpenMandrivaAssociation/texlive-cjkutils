# revision 26689
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-cjkutils
Version:	20120807
Release:	1
Summary:	TeXLive cjkutils package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cjkutils.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cjkutils.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-cjkutils.bin

%description
TeXLive cjkutils package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdir}/hbf2gf/README
%{_texmfdir}/hbf2gf/b5ka12.cfg
%{_texmfdir}/hbf2gf/b5kr12.cfg
%{_texmfdir}/hbf2gf/b5so12.cfg
%{_texmfdir}/hbf2gf/c1so12.cfg
%{_texmfdir}/hbf2gf/c2so12.cfg
%{_texmfdir}/hbf2gf/c3so12.cfg
%{_texmfdir}/hbf2gf/c4so12.cfg
%{_texmfdir}/hbf2gf/c5so12.cfg
%{_texmfdir}/hbf2gf/c6so12.cfg
%{_texmfdir}/hbf2gf/c7so12.cfg
%{_texmfdir}/hbf2gf/csso12.cfg
%{_texmfdir}/hbf2gf/gsfs14.cfg
%{_texmfdir}/hbf2gf/j2so12.cfg
%{_texmfdir}/hbf2gf/jsso12.cfg
%{_texmfdir}/hbf2gf/ksso17.cfg
%doc %{_texmfdir}/doc/bg5conv/bg5conv.pdf
%doc %{_texmfdir}/doc/cef5conv/cef5conv.pdf
%doc %{_texmfdir}/doc/cefconv/cefconv.pdf
%doc %{_texmfdir}/doc/cefsconv/cefsconv.pdf
%doc %{_texmfdir}/doc/extconv/extconv.pdf
%doc %{_texmfdir}/doc/hbf2gf/hbf2gf.pdf
%doc %{_mandir}/man1/bg5conv.1*
%doc %{_texmfdir}/doc/man/man1/bg5conv.man1.pdf
%doc %{_mandir}/man1/cef5conv.1*
%doc %{_texmfdir}/doc/man/man1/cef5conv.man1.pdf
%doc %{_mandir}/man1/cefconv.1*
%doc %{_texmfdir}/doc/man/man1/cefconv.man1.pdf
%doc %{_mandir}/man1/cefsconv.1*
%doc %{_texmfdir}/doc/man/man1/cefsconv.man1.pdf
%doc %{_mandir}/man1/extconv.1*
%doc %{_texmfdir}/doc/man/man1/extconv.man1.pdf
%doc %{_mandir}/man1/hbf2gf.1*
%doc %{_texmfdir}/doc/man/man1/hbf2gf.man1.pdf
%doc %{_mandir}/man1/sjisconv.1*
%doc %{_texmfdir}/doc/man/man1/sjisconv.man1.pdf
%doc %{_texmfdir}/doc/sjisconv/sjisconv.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120807-1
+ Revision: 812120
- Update to latest release.

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111103-2
+ Revision: 750250
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 718067
- texlive-cjkutils
- texlive-cjkutils
- texlive-cjkutils
- texlive-cjkutils
- texlive-cjkutils

