App = angular.module('App', ['ngAnimate'])

App.config ($httpProvider)->
  $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'

App.controller 'base', ($rootScope)->
    $rootScope.slidePageUrl = ''

    $rootScope.closePage = ()->
      $rootScope.slidePageUrl = ''

App.directive 'turbolink', ($http, $rootScope)->
  return {
    restrict: 'A'
    scope: false
    link: (scope, element, attrs)->
      element.on 'click', (event)->
        event.preventDefault()
        $rootScope.slidePageUrl = attrs.href
        scope.$digest()
      return
  }
