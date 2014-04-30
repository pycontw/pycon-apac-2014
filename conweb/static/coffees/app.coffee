App = angular.module('App', ['ngAnimate', 'ngCookies'])

App.config ($httpProvider)->
  $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'

App.controller 'base', ($rootScope, $scope)->
  $rootScope.slidePageUrl = ''

  $rootScope.closePage = (event)->
    if $rootScope.slidePageUrl == ''
      return
    $rootScope.slidePageUrl = ''
    return

  $scope.btnNavText = ()->
    if $scope.showNav
      return '✕'
    else
      return 'N'

  $scope.$on '$includeContentRequested', ()->
    $scope.loading = true

  $scope.$on '$includeContentLoaded', ()->
    $scope.loading = false


App.directive 'turbolink', ($http, $rootScope, $document)->
  return {
    restrict: 'A'
    scope: false
    link: (scope, element, attrs)->
      element.on 'click', (event)->
        event.preventDefault()
        if $rootScope.slidePageUrl != ''
          return
        event.stopPropagation()
        $rootScope.slidePageUrl = attrs.href
        scope.$digest()

      return
  }

App.directive 'foldList', ($cookieStore)->
  return {
    restrict: 'A'
    scope: false
    link: (scope, element, attrs)->
      li = element.find('li')

      if li.length == 0
        return

      foldSet = $cookieStore.get('foldSet') || {}
      id = attrs.foldList
      isFold = foldSet[id]

      foldIcon = angular.element('<fold>▾</fold>')
      element.append(foldIcon)


      fold = ()->
        element.addClass('fold')
        foldIcon.text('▸')

      unfold = ()->
        element.removeClass('fold')
        foldIcon.text('▾')

      if isFold
        fold()

      element.find('fold').on 'click', ()->
        isFold = !isFold
        foldSet[id] = isFold

        if isFold
          fold()
        else
          unfold()

        scope.$apply ()->
          $cookieStore.put('foldSet', foldSet)

        return

      return
  }
